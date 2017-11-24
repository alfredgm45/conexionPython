import json

# jsonData = '{"Nombre":"Alfredo","Cedula":23468856}'

# archivoJson =  open("datos.json","r")

def retornarArregloJsonPtyhon(nombrePlanta):

	with open("/opt/siog/"+nombrePlanta+"/puntosGalbaPrueba.json","r") as archivoJson:
		contenidoJson = archivoJson.read()

	# print(archivoJson.closed)
	jsonToPython = json.loads(contenidoJson)

	# print(len(jsonToPython))

	# i =0
	# while i <len(jsonToPython["Persona"]):
		
	# 	print(jsonToPython["Persona"][i]["Nombre"] +" "+ jsonToPython["Persona"][i]["Apellido"])
	# 	i = i+1

	return jsonToPython;
	
# pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
# dictionaryToJson = json.dumps(pythonDictionary) convertir un diccionario python a json

# print(dictionaryToJson)

# retornarArregloJsonPtyhon("taecjaa")
