import json 
import os
import time

i = 0 


# with open("indice.json","r+") as archivoJson:

# archivoJson = open("indice.json","r+")
# contenidoJson = archivoJson.read()
# archivoJson.seek(0)
# jsonToPython = json.loads(contenidoJson)

# jsonToPython["Numero"] = jsonToPython["Numero"]+1
# data = {"Numero":jsonToPython["Numero"]}
# archivoJson.write(json.dumps(data))
# print(json.dumps(contenidoJson))
# print(jsonToPython)
# archivoJson.close()

while i<11:
	os.system("python3 /home/alfredo/Documentos/conexionPython/tarea.py")
	i= i+1
	time.sleep(5)