import re
from collections import defaultdict
from datetime import datetime, timedelta

# Funzione per leggere il file di log con un encoding specifico
def leggi_log(file_path):
    try:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            lines = file.readlines()
            return lines
    except Exception as e:
        print(f"Errore nella lettura del file: {e}")
        return []

# Funzione per estrarre le informazioni da ciascuna riga del log
def estrai_informazioni(log_lines):
    pattern = re.compile(r'([^\s]+) - - \[([^\]]+)\] "GET (.*?) HTTP/1.0" (\d+) (\d+)')
    
    numero_visite_totali = 0  # Per contare il numero totale di richieste
    numero_righe_ignorate = 0
    numero_righe_analizzate = 0
    visite_per_ip = defaultdict(int)  # {ip: numero_visite}
    visite_per_pagina = defaultdict(int)  # {pagina: numero_visite}
    fasce_orarie = defaultdict(int)  # {ora: numero_visite}
    frequenza_collegamenti = defaultdict(int)  # {ip: numero_collegamenti}
    potenziali_ip_sospetti = defaultdict(int)  # {ip: numero_collegamenti_per_minuto}
    metodi_http = defaultdict(int)
    
    for line in log_lines:
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            timestamp = match.group(2)
            pagina = match.group(3)
            codice_risposta = match.group(4)
            byte_inviati = int(match.group(5))  # Quantità di byte inviati nella risposta
            
            # Estrazione della data e ora
            try:
                data_visita_str = timestamp.split(":")[0]  # Otteniamo solo la parte data, es: 01/Aug/1995
                data_visita = datetime.strptime(data_visita_str, '%d/%b/%Y')  # Es: 01/Aug/1995
                ora_visita = timestamp.split(":")[1]  # Es: 00 per l'orario
                minuto_visita = timestamp.split(":")[2].split()[0]  # Es: 01
                ora = f"{ora_visita}:{minuto_visita}"
            except ValueError:
                continue  # Se c'è un errore nel formato del timestamp, lo saltiamo
            
            # Incremento dei contatori
            numero_visite_totali += 1
            visite_per_ip[ip] += 1
            visite_per_pagina[pagina] += 1
            fasce_orarie[ora] += 1
            frequenza_collegamenti[ip] += 1
            potenziali_ip_sospetti[ip] += 1
            
            numero_righe_analizzate += 1
        else:
            numero_righe_ignorate += 1  # Incrementa il numero di righe ignorate
    
    return numero_visite_totali, numero_righe_ignorate, numero_righe_analizzate, visite_per_ip, visite_per_pagina, fasce_orarie, frequenza_collegamenti, potenziali_ip_sospetti

# Funzione per generare il report compatto e salvarlo su un file
def genera_report_compattato(file_path, numero_visite_totali, numero_righe_ignorate, numero_righe_analizzate, visite_per_ip, visite_per_pagina, fasce_orarie, frequenza_collegamenti, potenziali_ip_sospetti):
    with open(file_path, 'w') as report_file:
        # Report compatto
        report_file.write(f"Report  dei dati della NASA sui log: \n"
                          f"Numero totale di richieste nel log: {numero_visite_totali + numero_righe_ignorate} \n "
                          f"Numero totale di visite: {numero_visite_totali} \n "
                          f"Numero di richieste ignorate: {numero_righe_ignorate} \n "
                          f"Numero di richieste analizzate correttamente: {numero_righe_analizzate}\n")
        
        # Metodi HTTP
        report_file.write("Distribuzione richieste HTTP:\n")
        for metodo, conteggio in metodi_http.items():
            report_file.write(f"{metodo}: {conteggio}\n")
        report_file.write("\n")
        
        # Top 10 IP/Domini con più richieste
        top_ips = sorted(visite_per_ip.items(), key=lambda x: x[1], reverse=True)[:10]
        top_ips_result = "\n" + "Top 10 IP/Domini: " + " \n ".join([f"{ip}: {richieste}" for ip, richieste in top_ips])
        report_file.write(top_ips_result + "\n")
        
        # Top 10 pagine più visitate
        top_pagine = sorted(visite_per_pagina.items(), key=lambda x: x[1], reverse=True)[:10]
        top_pagine_result = "\n" + "Top 10 Pagine: " + " \n ".join([f"{pagina}: {visite}" for pagina, visite in top_pagine])
        report_file.write(top_pagine_result + "\n")
        
        # Top 10 fasce orarie più trafficate
        top_fasce = sorted(fasce_orarie.items(), key=lambda x: x[1], reverse=True)[:10]
        top_fasce_result = "\n" + "Top 10 Fasce Orarie: " + " \n ".join([f"{fascia}: {traffico}" for fascia, traffico in top_fasce])
        report_file.write(top_fasce_result + "\n")
        
        # Potenziali IP sospetti (frequenza di richieste > 100 in un minuto)
        top_sospetti = sorted(potenziali_ip_sospetti.items(), key=lambda x: x[1], reverse=True)[:10]
        if top_sospetti:
            report_file.write("\n" + "Top 10 IP sospetti: " + " \n ".join([f"{ip}: {richieste}" for ip, richieste in top_sospetti]) + "\n")
        else:
            report_file.write("Top 10 IP sospetti: Nessuno trovato\n")


    report_file.write(f"\n \n \n Conclusioni L'analisi evidenzia un elevato numero di richieste relative a loghi e immagini, suggerendo una forte presenza di accessi automatici o di caching da parte di browser e proxy. Gli IP più attivi coincidono con quelli considerati sospetti, il che potrebbe indicare traffico non del tutto legittimo o picchi di richieste anomale. Le fasce orarie più trafficate si concentrano nel primo pomeriggio, suggerendo possibili correlazioni con attività lavorative o di ricerca. Ulteriori analisi potrebbero essere necessarie per individuare eventuali anomalie o attività malevole nei dati raccolti.\n \n")

# Funzione principale
def main(file_path):
    log_lines = leggi_log(file_path)
    if not log_lines:
        print("Errore: Il file di log non è stato letto correttamente.")
        return
    
    numero_visite_totali, numero_righe_ignorate, numero_righe_analizzate, visite_per_ip, visite_per_pagina, fasce_orarie, frequenza_collegamenti, potenziali_ip_sospetti = estrai_informazioni(log_lines)
    if numero_visite_totali == 0:
        print("Nessun dato trovato nel log.")
        return
    
    genera_report_compattato('report.dmp', numero_visite_totali, numero_righe_ignorate, numero_righe_analizzate, visite_per_ip, visite_per_pagina, fasce_orarie, frequenza_collegamenti, potenziali_ip_sospetti)

if __name__ == "__main__":
    # Specifica il percorso del file di log
    file_path = "/home/user/RiccardoRusso/Sicurezza3/Esercizio/NASA_access_log_Aug95"  # Sostituisci con il percorso del tuo file di log
    main(file_path)
