import re
from collections import defaultdict
from datetime import datetime, timedelta

# Funzione per leggere il file di log con un encoding specifico
def leggi_log(file_path):
    try:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            lines = file.readlines()
            print("Prime 5 righe del file di log:")
            for line in lines[:5]:
                print(line)
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
    righe_processate = 0
    
    for line in log_lines:
        match = pattern.search(line)
        if match:
            righe_processate += 1
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

# Funzione per generare il report
def genera_report(numero_visite_totali, numero_righe_ignorate, numero_righe_analizzate, visite_per_ip, visite_per_pagina, fasce_orarie, frequenza_collegamenti, potenziali_ip_sospetti):
    print("### Report Generato ###")

    # Numero totale di richieste nel log
    print(f"\nNumero totale di richieste nel log: {numero_visite_totali + numero_righe_ignorate}")
    
    # Numero totale di visite
    print(f"\nNumero totale di visite: {numero_visite_totali}")
    
    # Numero totale visite per pagina
    print("\nNumero totale visite per pagina:")
    for pagina, visite in sorted(visite_per_pagina.items(), key=lambda x: x[1], reverse=True):
        print(f"  Pagina: {pagina} -> Visite: {visite}")
    
    # Numero di richieste ignorate
    print(f"\nNumero di richieste ignorate (formato non valido): {numero_righe_ignorate}")
    
    # Numero di richieste analizzate correttamente
    print(f"\nNumero di richieste analizzate correttamente: {numero_righe_analizzate}")
    
    # Top 10 IP/Domini con più richieste
    print("\nTop 10 IP/Domini con più richieste:")
    for ip, richieste in sorted(visite_per_ip.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  IP/Dominio: {ip} -> Richieste: {richieste}")
    
    # Top 10 pagine più visitate
    print("\nTop 10 Pagine più visitate:")
    for pagina, visite in sorted(visite_per_pagina.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  Pagina: {pagina} -> Visite: {visite}")
    
    # Top 10 fasce orarie più trafficate
    print("\nTop 10 Fasce orarie più trafficate:")
    for fascia, traffico in sorted(fasce_orarie.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  Fascia Oraria: {fascia} -> Traffico: {traffico}")
    
    # Potenziali IP sospetti (frequenza di richieste > 100 in un minuto)
    print("\nPotenziali IP sospetti:")
    for ip, richieste in sorted(potenziali_ip_sospetti.items(), key=lambda x: x[1], reverse=True):
        if richieste > 100:
            print(f"  IP: {ip} -> Richieste in un minuto: {richieste}")

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
    
    genera_report(numero_visite_totali, numero_righe_ignorate, numero_righe_analizzate, visite_per_ip, visite_per_pagina, fasce_orarie, frequenza_collegamenti, potenziali_ip_sospetti)

if __name__ == "__main__":
    # Specifica il percorso del file di log
    file_path = "/home/user/RiccardoRusso/Sicurezza3/Esercizio/NASA_access_log_Aug95"  # Sostituisci con il percorso del tuo file di log
    main(file_path)
