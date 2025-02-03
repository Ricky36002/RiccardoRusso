from flask import Flask, request, jsonify
from myjson import JsonSerialize, JsonDeserialize
import json
import logging

sFileDati = "./EsDizionario.json"
api = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

def carica_dati():
    try:
        with open('EsDizionario.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("File 'data.json' non trovato.")
        return {"case_in_vendita": [], "case_in_affitto": [], "vendite": [], "affitti": []}
    except json.JSONDecodeError:
        logging.error("Errore nel decodificare il file JSON.")
        return {"case_in_vendita": [], "case_in_affitto": [], "vendite": [], "affitti": []}

def salva_dati(data):
    try:
        with open('EsDizionario.json', 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        logging.error(f"Errore durante il salvataggio dei dati: {e}")

@api.route('/CercaCasaVendita', methods=['POST'])
def cerca_casa_vendita():
    try:
        data = request.get_json()
        prezzo_min = data.get('prezzo_min')
        prezzo_max = data.get('prezzo_max')
        metri_min = data.get('metri_min')
        metri_max = data.get('metri_max')
        stato = data.get('stato')

        db = carica_dati()
        case_trovate = [casa for casa in db['case_in_vendita'] if
                        prezzo_min <= casa['prezzo'] <= prezzo_max and
                        metri_min <= casa['metri'] <= metri_max and
                        casa['stato'] == stato]

        return jsonify(case_trovate)

    except Exception as e:
        logging.error(f"Errore nella richiesta di ricerca case in vendita: {e}")
        return jsonify({"error": "Errore durante la ricerca delle case in vendita"}), 500

@api.route('/CercaCasaAffitto', methods=['POST'])
def cerca_casa_affitto():
    try:
        data = request.get_json()
        prezzo_min = data.get('prezzo_min')
        prezzo_max = data.get('prezzo_max')
        tipo_affitto = data.get('tipo_affitto')

        db = carica_dati()
        case_trovate = [casa for casa in db['case_in_affitto'] if
                        prezzo_min <= casa['prezzo_mensile'] <= prezzo_max and
                        casa['tipo_affitto'] == tipo_affitto]

        return jsonify(case_trovate)

    except Exception as e:
        logging.error(f"Errore nella richiesta di ricerca case in affitto: {e}")
        return jsonify({"error": "Errore durante la ricerca delle case in affitto"}), 500


    
@api.route('/VendutaCasa', methods=['POST'])
def venduta_casa():
    vendita = request.get_json()['vendita']
    print(vendita)

    data = JsonDeserialize(sFileDati)
    
    print (data["case_in_vendita"][0])
    
    for casa in data.get("case_in_vendita", []):
        print(casa["catastale"])
        print(vendita["catastale"])
        

        if casa["catastale"] == vendita["catastale"]:
            data.setdefault("vendite_casa", []).append({
                "catastale": vendita["catastale"],
                "data_vendita": vendita["data_vendita"],
                "filiale_proponente": vendita["filiale_proponente"],
                "filiale_venditrice": vendita["filiale_venditrice"],
                "prezzo_vendita": vendita["prezzo_vendita"]
            })
            data["case_in_vendita"].remove(casa)
            for filiale in data.get("filiali", []):
                if filiale["partita_iva"] == vendita["filiale_venditrice"]:
                    filiale["case_vendute"] = filiale.get("case_vendute", 0) + 1
            JsonSerialize(data, sFileDati)
            return jsonify({"message": "Vendita registrata con successo."}), 200

    return jsonify({"error": "Casa non trovata."}), 404

@api.route('/AffittataCasa', methods=['POST'])
def affittata_casa():
    affitto = request.get_json()['affitto']
    print(affitto)
    data = JsonDeserialize(sFileDati)

    for casa in data.get("case_in_affitto", []):
        if casa["catastale"] == affitto["catastale"]:
            data.setdefault("affitti_casa", []).append({
                "catastale": affitto["catastale"],
                "data_affitto": affitto["data_affitto"],
                "filiale_proponente": affitto["filiale_proponente"],
                "filiale_venditrice": affitto["filiale_venditrice"],
                "prezzo_affitto": affitto["prezzo_affitto"],
                "durata_contratto": affitto["durata_contratto"]
            })
            data["case_in_affitto"].remove(casa)
            for filiale in data.get("filiali", []):
                if filiale["partita_iva"] == affitto["filiale_venditrice"]:
                    filiale["case_affittate"] = filiale.get("case_affittate", 0) + 1
            JsonSerialize(data, sFileDati)
            return jsonify({"message": "Affitto registrato con successo."}), 200

    return jsonify({"error": "Casa non trovata."}), 404

if __name__ == '__main__':
    api.run(debug=True, port = 8080)
