import requests
import subprocess
import urllib3
import myjson

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sModel = "gemini-1.5-flash-latest"
base_url = "https://generativelanguage.googleapis.com/v1beta/models/" + sModel + ":generateContent?key="
with open("GoogleAPIKey.txt","r") as file:
    GoogleAPIKey = file.read() 
api_url = base_url + GoogleAPIKey

def ComponiJsonPerImmagine(sImagePath):
  subprocess.run(["cp", sImagePath,"./temp_img/image.jpg"])
  subprocess.run(["bash", "./creajsonpersf.sh"])

def CercaIMGGemini(sFile, sArgomento):
    ComponiJsonPerImmagine(sFile)
    dJsonRequest = myjson.JsonDeserialize("request.json")
    dJsonRequest["contents"][0]["parts"][0]["text"] = f"Rispondere soltanto 'True.' o 'False.'. Quest'immagine centra qualcosa con {sArgomento}?"
    response = requests.post(api_url,json=dJsonRequest, verify=False)
    if response.status_code==200:
        dResponse = response.json()
        dListaContenuti = dResponse["candidates"][0]["content"]["parts"][0]["text"].strip(".")
        if dListaContenuti == "True":
            return True
        else:
            return False
    else:
        print(f"Error {response.status_code}: {response.text}")