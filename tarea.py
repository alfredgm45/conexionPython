import json 
import os
import time


# print ("Start : "+time.ctime())

# print ("End : "+time.ctime())
#time.sleep()


archivoJson = open("/home/alfredo/Documentos/conexionPython/indice.json","r+")
contenidoJson = archivoJson.read()
archivoJson.seek(0)
jsonToPython = json.loads(contenidoJson)

jsonToPython["Numero"] = jsonToPython["Numero"]+1
data = {"Numero":jsonToPython["Numero"]}
archivoJson.write(json.dumps(data))
print(json.dumps(contenidoJson))
print(jsonToPython)
archivoJson.close()

os.system("cd /home/alfredo/Documentos/conexionPython/prueba;touch hola"+str(jsonToPython["Numero"])+".txt")

 