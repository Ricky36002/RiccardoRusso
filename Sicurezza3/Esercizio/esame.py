import re
from collections import defaultdict
from datetime import datetime

# Funzione per leggere il file di log
def leggi_log(file_path):
    with open(file_path, 'r', encoding='ISO-8859-1') as file:  # Modificato l'encoding
        return file.readlines()

# Funzione per estrarre le informazioni da ciascuna riga del log
def estrai_informazioni(log_lines):
    # Regex per estrarre informazioni da una riga del log
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[([^\]]+)\] "GET (.*?) HTTP/1.1" (\d+) (\d+)')
    
    visite_giornaliere = defaultdict(lambda: defaultdict(int))  # {giorno: {ip: numero_visite}}
    visite_per_pagina = defaultdict(int)  # {pagina: numero_visite}
    frequenza_collegamenti = defaultdict(int)  # {ip: numero_collegamenti}
    
    for line in log_lines:
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            timestamp = match.group(2)
            pagina = match.group(3)
            data_visita = datetime.strptime(timestamp.split()[0], '%d/%b/%Y')  # Es: 01/Aug/1995
            giorno = data_visita.date()
            
            # Contare le visite per giorno, ip e pagina
            visite_giornaliere[giorno][ip] += 1
            visite_per_pagina[pagina] += 1
            frequenza_collegamenti[ip] += 1
    
    return visite_giornaliere, visite_per_pagina, frequenza_collegamenti

# Funzione per generare il report giornaliero
def genera_report_giornaliero(visite_giornaliere, visite_per_pagina, frequenza_collegamenti):
    print("### Report Giornaliero ###")
    
    # Report visite giornaliere per IP/dominio
    print("\nVisite per giorno e IP/dominio:")
    for giorno, ip_visite in sorted(visite_giornaliere.items()):
        print(f"\nData: {giorno}")
        for ip, visite in ip_visite.items():
            print(f"  IP: {ip} -> Visite: {visite}")
    
    # Report pagine visitate
    print("\nVisite per pagina:")
    for pagina, visite in sorted(visite_per_pagina.items(), key=lambda x: x[1], reverse=True):
        print(f"  Pagina: {pagina} -> Visite: {visite}")
    
    # Report frequenza di collegamento per IP
    print("\nFrequenza di collegamento per IP:")
    for ip, collegamenti in sorted(frequenza_collegamenti.items(), key=lambda x: x[1], reverse=True):
        print(f"  IP: {ip} -> Collegamenti: {collegamenti}")

# Funzione per generare il report mensile
def genera_report_mensile(visite_giornaliere, visite_per_pagina, frequenza_collegamenti):
    print("\n### Report Mensile ###")
    
    # Report visite mensili per IP/dominio
    visite_mensili = defaultdict(int)  # {ip: numero_visite}
    for giorno, ip_visite in visite_giornaliere.items():
        for ip, visite in ip_visite.items():
            visite_mensili[ip] += visite
    
    print("\nVisite per IP/dominio (mensile):")
    for ip, visite in sorted(visite_mensili.items(), key=lambda x: x[1], reverse=True):
        print(f"  IP: {ip} -> Visite: {visite}")
    
    # Report pagine visitate mensili
    print("\nVisite per pagina (mensile):")
    for pagina, visite in sorted(visite_per_pagina.items(), key=lambda x: x[1], reverse=True):
        print(f"  Pagina: {pagina} -> Visite: {visite}")
    
    # Report frequenza di collegamento mensile per IP
    print("\nFrequenza di collegamento per IP (mensile):")
    for ip, collegamenti in sorted(frequenza_collegamenti.items(), key=lambda x: x[1], reverse=True):
        print(f"  IP: {ip} -> Collegamenti: {collegamenti}")

# Funzione principale
def main(file_path):
    log_lines = leggi_log(file_path)
    visite_giornaliere, visite_per_pagina, frequenza_collegamenti = estrai_informazioni(log_lines)
    genera_report_giornaliero(visite_giornaliere, visite_per_pagina, frequenza_collegamenti)
    genera_report_mensile(visite_giornaliere, visite_per_pagina, frequenza_collegamenti)

if __name__ == "__main__":
    # Specifica il percorso del file di log
    file_path = "/home/user/RiccardoRusso/Sicurezza3/Esercizio/NASA_access_log_Aug95"  # Sostituisci con il percorso del tuo file di log
    main(file_path)
