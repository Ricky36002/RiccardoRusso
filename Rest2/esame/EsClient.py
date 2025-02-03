import requests
import json

def cerca_case_vendita():
    print("\n--- Cerca Casa in Vendita ---")
    prezzo_min = float(input("Prezzo minimo: "))
    prezzo_max = float(input("Prezzo massimo: "))
    metri_min = float(input("Metri quadrati minimi: "))
    metri_max = float(input("Metri quadrati massimi: "))
    vani_min = float(input("Vani minimi: "))
    vani_max = float(input("Vani massimi: "))
    piano = float(input("piano: "))
    stato = input("Stato (LIBERO/OCCUPATO): ").upper()

    dati = {
        "prezzo_min": prezzo_min,
        "prezzo_max": prezzo_max,
        "metri_min": metri_min,
        "metri_max": metri_max,
        "vani_min": vani_min,
        "vani_max": vani_max,
        "piano": piano,
        "stato": stato
    }

    try:
        response = requests.post("http://127.0.0.1:8080/CercaCasaVendita", json=dati)
        if response.status_code == 200:
            case = response.json()
            print("\nCase in vendita trovate:")
            if case:
                for casa in case:
                    print(f"- {casa['catastale']} {casa['indirizzo']}{casa['numero_civico']} ({casa['stato']})")
            else:
                print("Nessuna casa trovata con i criteri specificati.")
        else:
            print("Errore nella richiesta:", response.status_code)
    except Exception as e:
        print(f"Errore nella richiesta: {e}")

def cerca_case_affitto():
    print("\n--- Cerca Casa in Affitto ---")
    prezzo_min = float(input("Prezzo minimo mensile: "))
    prezzo_max = float(input("Prezzo massimo mensile: "))
    metri_min = float(input("Metri quadrati minimi: "))
    metri_max = float(input("Metri quadrati massimi: "))
    vani_min = float(input("Vani minimi: "))
    vani_max = float(input("Vani massimi: "))
    piano = float(input("piano: "))
    tipo_affitto = input("Tipo di affitto (PARZIALE/TOTALE): ").upper()

    dati = {
        "prezzo_min": prezzo_min,
        "prezzo_max": prezzo_max,
        "metri_min": metri_min,
        "metri_max": metri_max,
        "vani_min": vani_min,
        "vani_max": vani_max,
        "piano": piano,
        "tipo_affitto": tipo_affitto
    }

    try:
        response = requests.post("http://127.0.0.1:8080/CercaCasaAffitto", json=dati)
        if response.status_code == 200:
            case = response.json()
            print("\nCase in affitto trovate:")
            if case:
                for casa in case:
                    print(f"- {casa['catastale']} {casa['indirizzo']} {casa['numero_civico']} ({casa['tipo_affitto']})")
            else:
                print("Nessuna casa trovata con i criteri specificati.")
        else:
            print("Errore nella richiesta:", response.status_code)
    except Exception as e:
        print(f"Errore nella richiesta: {e}")

def registrare_vendita():
    print("\n--- Registrare una Vendita ---")
    catastale = input("Codice catastale della casa: ")
    data_vendita = input("Data della vendita (YYYY-MM-DD): ")
    filiale_proponente = input("Filiale proponente: ")
    filiale_venditrice = input("Filiale venditrice: ")
    prezzo_vendita = float(input("Prezzo di vendita: "))

    dati_vendita = {
        "vendita": {
            "catastale": catastale,
            "data_vendita": data_vendita,
            "filiale_proponente": filiale_proponente,
            "filiale_venditrice": filiale_venditrice,
            "prezzo_vendita": prezzo_vendita
        }
    }

    try:
        response = requests.post("http://127.0.0.1:8080/VendutaCasa", json=dati_vendita)
        print("okokok")
        print(response.status_code)
        if response.status_code == 200:
            print("\nVendita registrata con successo!")
        else:
            print("Errore nella registrazione della vendita:", response.status_code)
    except Exception as e:
        print(f"Errore 2 nella registrazione della vendita: {e}")

def registrare_affitto():
    print("\n--- Registrare un Affitto ---")
    catastale = input("Codice catastale della casa: ")
    data_affitto = input("Data dell'affitto (YYYY-MM-DD): ")
    filiale_proponente = input("Filiale proponente: ")
    filiale_venditrice = input("Filiale affittante: ")
    prezzo_affitto = float(input("Prezzo mensile affitto: "))
    durata_contratto = input("Durata del contratto (in mesi): ")

    dati_affitto = {
        "affitto": {
            "catastale": catastale,
            "data_affitto": data_affitto,
            "filiale_proponente": filiale_proponente,
            "filiale_venditrice": filiale_venditrice,
            "prezzo_affitto": prezzo_affitto,
            "durata_contratto": durata_contratto
        }
    }

    try:
        response = requests.post("http://127.0.0.1:8080/AffittataCasa", json=dati_affitto)
        if response.status_code == 200:
            print("\nAffitto registrato con successo!")
        else:
            print("Errore nella registrazione dell'affitto:", response.status_code)
    except Exception as e:
        print(f"Errore nella registrazione dell'affitto: {e}")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Cerca case in vendita")
        print("2. Cerca case in affitto")
        print("3. Registrare una vendita")
        print("4. Registrare un affitto")
        print("5. Esci")

        scelta = input("Scegli un'opzione (1-5): ")

        if scelta == '1':
            cerca_case_vendita()
        elif scelta == '2':
            cerca_case_affitto()
        elif scelta == '3':
            registrare_vendita()
        elif scelta == '4':
            registrare_affitto()
        elif scelta == '5':
            print("Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")
            

if __name__ == "__main__":
    menu()
