import subprocess 
import sys


#obtengo el proceso del script que ejecuta la adquisicion de los datos
archivo = "/opt/siog/"

def tratamientoString(cadena):
	cadena = cadena.lstrip("b'")
	cadena = cadena.rstrip("'")
	cadena = cadena.rstrip("n")
	cadena = cadena.rstrip("\~")

	return cadena 
# valorPuntoAnalogico =  str(subprocess.check_output("awk '/06TA1T09_H20_SM/,/36554433/ {print substr($12,14)}' "+html, shell=True))
# valorPuntoAnalogico = tratamientoString(valorPuntoAnalogico)
# valorPuntoAnalogico.append(str(subprocess.check_output("awk '/"+puntosA[i][0]["tag_name"]+"/,/"+puntosA[i][0]["point_id"]+"/ \
# 	{print substr($12,14)}' "+html, shell=True)))
# i = i+1	
def retornarValorPuntoAnalogico(nombrePlanta,puntos,coordenadas):

	html = archivo+nombrePlanta+"/AcquisitionData.html"
	valor = archivo+nombrePlanta+"/fichero.txt"

	i = 0
	j = 0
	valorPuntoAnalogico =[]
	while i < len(puntos):
		
		
		if i == coordenadas[j]:

			
			valorPuntoAnalogico.append(str(subprocess.check_output("awk '/"+str(puntos[i][0]["point_id"])+"/ \
				{print substr($12,14)}' "+html+" >"+valor+"; awk 'NR==1' "+valor, shell=True)))
			if j < len(coordenadas)-1:
			
				j=j+1

		i = i +1

	i = 0 

	while i < len(valorPuntoAnalogico):
	 	valorPuntoAnalogico[i] = tratamientoString(valorPuntoAnalogico[i])
	 	i = i+1
	return valorPuntoAnalogico
		
 	


	


# calidadPuntoAnalogico= str(subprocess.check_output("awk '/06TA1T09_H20_SM/,/36554433/ {print substr($16,14)}' "+html, shell=True))
# calidadPuntoAnalogico = tratamientoString(calidadPuntoAnalogico)

def retornarCalidadPuntoAnalogico(nombrePlanta,puntos,coordenadas):
	
	html = archivo+nombrePlanta+"/AcquisitionData.html"
	valor = archivo+nombrePlanta+"/fichero.txt"
	i = 0
	j = 0
	calidadPuntoAnalogico =[]
	while i < len(puntos):
		
		
		
		if i == coordenadas[j]:

			
			calidadPuntoAnalogico.append(str(subprocess.check_output("awk '/"+str(puntos[i][0]["point_id"])+"/ \
				{print substr($16,14)}' "+html+" >"+valor+"; awk 'NR==1' "+valor, shell=True)))
			if j < len(coordenadas)-1:
			
				j=j+1

		i = i +1
	
	i = 0 
	
	while i < len(calidadPuntoAnalogico):
	 	calidadPuntoAnalogico[i] = tratamientoString(calidadPuntoAnalogico[i])
	 	i = i+1
	
	return calidadPuntoAnalogico

# estadoPuntoDigital = str(subprocess.check_output("awk '/06MV-1091_FE/,/36554434/ {print substr($14,14)}' "+html, shell=True))
# print(retornarCalidadPuntoAnalogico("taecjaa",""))

def retornarEstadoPuntoDigital(nombrePlanta,puntos,coordenadas):
	
	valor = archivo+nombrePlanta+"/fichero.txt"
	html = archivo+nombrePlanta+"/AcquisitionData.html"
	i = 0
	j = 0
	estadoPuntoDigital =[]
	while i < len(puntos):
		
		
		if i == coordenadas[j]:

			
			estadoPuntoDigital.append(str(subprocess.check_output("awk '/"+str(puntos[i][0]["point_id"])+"/ \
				{print substr($14,14)}' "+html+" >"+valor+"; awk 'NR==1' "+valor, shell=True)))
			if j < len(coordenadas)-1:
			
				j=j+1

		i = i +1

	i = 0 

	while i < len(estadoPuntoDigital):
	 	estadoPuntoDigital[i] = tratamientoString(estadoPuntoDigital[i])
	 	i = i+1
	return estadoPuntoDigital



# calidadPuntoDigital = str(subprocess.check_output("awk '/06MV-1091_FE/,/36554434/ {print substr($21,14)}' "+html, shell=True))
	# calidadPuntoDigital = tratamientoString(calidadPuntoDigital)

def retornarCalidadPuntoDigital(nombrePlanta,puntos,coordenadas):
	
	html = archivo+nombrePlanta+"/AcquisitionData.html"
	valor = archivo+nombrePlanta+"/fichero.txt"
	i = 0
	j = 0

	calidadPuntoDigital = []

	while i < len(puntos):
		
		
		if i == coordenadas[j]:

			
			calidadPuntoDigital.append(str(subprocess.check_output("awk '/"+str(puntos[i][0]["point_id"])+"/ \
				{print substr($21,14)}' "+html+" >"+valor+"; awk 'NR==1' "+valor, shell=True)))
			if j < len(coordenadas)-1:
			
				j=j+1

		i = i +1

	i = 0 

	while i < len(calidadPuntoDigital):
	 	calidadPuntoDigital[i] = tratamientoString(calidadPuntoDigital[i])
	 	i = i+1

	return calidadPuntoDigital





