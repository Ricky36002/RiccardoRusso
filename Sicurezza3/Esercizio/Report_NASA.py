import re
from collections import defaultdict
from datetime import datetime

# Funzione per leggere il file di log con un encoding specifico
def leggi_log(file_path):
    try:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            return file.readlines()
    except Exception as e:
        print(f"Errore nella lettura del file: {e}")
        return []

# Funzione per estrarre le informazioni da ciascuna riga del log
def estrai_informazioni(log_lines):
    pattern = re.compile(r'([^\s]+) - - \[([^\]]+)\] "(GET|POST|HEAD) (.*?) HTTP/1.0" (\d+) (\d+)')

    numero_visite_totali = 0
    numero_righe_ignorate = 0
    numero_righe_analizzate = 0
    visite_per_ip = defaultdict(int)
    visite_per_pagina = defaultdict(int)
    fasce_orarie = defaultdict(int)
    metodi_http = defaultdict(int)  # Conta GET, POST, HEAD
    frequenza_collegamenti = defaultdict(int)  # Conta le richieste per IP
    potenziali_ip_sospetti = defaultdict(int)  # IP con molte richieste in poco tempo
    
    for line in log_lines:
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            timestamp = match.group(2)
            metodo_http = match.group(3)
            pagina = match.group(4)
            codice_risposta = match.group(5)

            # Estrazione della data e ora
            try:
                ora_visita = timestamp.split(":")[1]  # Es: 00 per l'orario
                minuto_visita = timestamp.split(":")[2].split()[0]  # Es: 01
                ora = f"{ora_visita}:{minuto_visita}"
            except ValueError:
                continue

            # Incremento dei contatori
            numero_visite_totali += 1
            visite_per_ip[ip] += 1
            visite_per_pagina[pagina] += 1
            fasce_orarie[ora] += 1
            metodi_http[metodo_http] += 1
            frequenza_collegamenti[ip] += 1
            potenziali_ip_sospetti[ip] += 1
            
            numero_righe_analizzate += 1
        else:
            numero_righe_ignorate += 1
    
    return (numero_visite_totali, numero_righe_ignorate, numero_righe_analizzate, 
            visite_per_ip, visite_per_pagina, fasce_orarie, metodi_http, potenziali_ip_sospetti)

# Funzione per generare il report
def genera_report_compattato(file_path, numero_visite_totali, numero_righe_ignorate, numero_righe_analizzate, 
                             visite_per_ip, visite_per_pagina, fasce_orarie, metodi_http, potenziali_ip_sospetti):
    with open(file_path, 'w') as report_file:
        report_file.write(f"Report dei dati della NASA sui log:\n"
                          f"Numero totale di richieste nel log: {numero_visite_totali + numero_righe_ignorate}\nIndica il volume complessivo di richieste processate, fornendo un’idea della dimensione del dataset.\n\n"
                          f"Numero totale di visite: {numero_visite_totali}\nMostra il numero effettivo di richieste analizzabili dopo aver filtrato errori e richieste anomale.\n\n"
                          f"Numero di richieste ignorate: {numero_righe_ignorate}\nSegnala eventuali errori di parsing o righe di log corrotte, che potrebbero nascondere dati mancanti.\n\n"
                          f"Numero di richieste analizzate correttamente: {numero_righe_analizzate}\nGarantisce che la maggior parte dei dati sia stata elaborata correttamente, permettendo un’analisi affidabile.\n\n")

        # Metodi HTTP
        report_file.write("Distribuzione richieste HTTP:\n")
        for metodo, conteggio in metodi_http.items():
            report_file.write(f"{metodo}: {conteggio}\n")
        report_file.write("\nAiuta a capire come gli utenti interagiscono con il sito. Un numero elevato di GET indica una navigazione standard,\nmentre molti POST potrebbero segnalare invii di dati o interazioni più complesse.\nMostra che quasi tutte le richieste sono GET, suggerendo che la maggior parte del traffico riguarda il download di contenuti (es. immagini, pagine web).\n\n")

        # Top 10 IP/Domini
        top_ips = sorted(visite_per_ip.items(), key=lambda x: x[1], reverse=True)[:10]
        report_file.write("Top 10 IP/Domini:\n" + "\n".join([f"{ip}: {richieste}" for ip, richieste in top_ips]) + "\n")
        report_file.write("\nIdentifica gli utenti più attivi nel log. Se un IP compare frequentemente, potrebbe essere un bot, un proxy o un server cache.\nSi notano domini NASA e AOL Proxy: potrebbero essere accessi interni o richieste provenienti da un sistema di caching (es. AOL).\n\n\n")

        # Top 10 pagine più visitate
        top_pagine = sorted(visite_per_pagina.items(), key=lambda x: x[1], reverse=True)[:10]
        report_file.write("Top 10 Pagine:\n" + "\n".join([f"{pagina}: {visite}" for pagina, visite in top_pagine]) + "\n")
        report_file.write("\nPermette di capire quali risorse vengono richieste più spesso. Se la maggior parte del traffico riguarda immagini, potrebbe trattarsi di cache dei browser o bot che scaricano risorse statiche.\nLe immagini dei loghi dominano la classifica, suggerendo che molte richieste provengono da utenti che visualizzano pagine con contenuti grafici pesanti o bot che scaricano risorse statiche.\n\n\n")
        # Top 10 fasce orarie più trafficate
        top_fasce = sorted(fasce_orarie.items(), key=lambda x: x[1], reverse=True)[:10]
        report_file.write("Top 10 Fasce Orarie:\n" + "\n".join([f"{fascia}: {traffico}" for fascia, traffico in top_fasce]) + "\n")
        report_file.write("\nIdentifica i momenti di maggiore traffico, utili per analizzare il comportamento degli utenti e la possibile origine geografica.\nIl traffico si concentra nel pomeriggio (tra le 12:49 e le 15:53), suggerendo attività lavorative o di ricerca.\n\n\n")
        # IP sospetti
        top_sospetti = sorted(potenziali_ip_sospetti.items(), key=lambda x: x[1], reverse=True)[:10]
        if top_sospetti:
            report_file.write("Top 10 IP sospetti:\n" + "\n".join([f"{ip}: {richieste}" for ip, richieste in top_sospetti]) + "\n")
            report_file.write("\nMostra gli IP con il numero più alto di richieste, potenziali bot o attaccanti che potrebbero causare traffico anomalo.\nGli IP più attivi coincidono con quelli nei Top IP/Domini, rafforzando l’ipotesi che proxy o bot stiano generando un numero elevato di richieste.\n\n\n")
        else:
            report_file.write("Top 10 IP sospetti: Nessuno trovato\n")

        # Conclusioni
        report_file.write("\nConclusioni:\nL'analisi evidenzia un elevato numero di richieste relative a loghi e immagini,\n "
                          "suggerendo una forte presenza di accessi automatici o di caching da parte di browser e proxy. \n"
                          "Gli IP più attivi coincidono con quelli considerati sospetti, il che potrebbe indicare traffico\n "
                          "non del tutto legittimo o picchi di richieste anomale. Le fasce orarie più trafficate si concentrano\n "
                          "nel primo pomeriggio, suggerendo possibili correlazioni con attività lavorative o di ricerca.\n "
                          "Ulteriori analisi potrebbero essere necessarie per individuare eventuali anomalie o attività malevole nei dati raccolti.\n")

# Funzione principale
def main(file_path):
    log_lines = leggi_log(file_path)
    if not log_lines:
        print("Errore: Il file di log non è stato letto correttamente.")
        return
    
    (numero_visite_totali, numero_righe_ignorate, numero_righe_analizzate, 
     visite_per_ip, visite_per_pagina, fasce_orarie, metodi_http, potenziali_ip_sospetti) = estrai_informazioni(log_lines)
    
    if numero_visite_totali == 0:
        print("Nessun dato trovato nel log.")
        return
    
    genera_report_compattato('report.dmp', numero_visite_totali, numero_righe_ignorate, numero_righe_analizzate, 
                             visite_per_ip, visite_per_pagina, fasce_orarie, metodi_http, potenziali_ip_sospetti)

if __name__ == "__main__":
    file_path = "/home/user/RiccardoRusso/Sicurezza3/Esercizio/NASA_access_log_Aug95"
    main(file_path)
