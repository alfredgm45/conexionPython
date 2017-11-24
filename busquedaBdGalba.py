from conexionDB import conexionDB
# conexion a la  base de datos GALBA (servidor mirrow)
galba = conexionDB()
galba.parametrosConexion("GALBA","postgres","root","localhost")
galba.conectar()

# Entrada de los puntos selecccioados por el administrador operativo
# puntos = {"point_id":"36554433"},{"point_id":"36554434"},{"point_id":"36554435"},\
# 		{"point_id":"36554436"},{"point_id":"36554437"}

def imprimirValores(arreglo):
	i = 0	

	while i<len(arreglo):
		print(arreglo[i])
		i = i+1


def busquedaPuntos(puntos):
	# Diccionario que almacena los puntos de la tabla point
	points = {}

	# Busqueda de los puntos en la base datos galba 
	i = 0
	agregado = 0

	while i<len(puntos):
		valor = galba.retornarConsulta("select point_id, tag_name, point_description, data_type_id from point where point_id="\
			+str(puntos[i]))
		
		
		if len(valor)!=0:

			points[agregado] = valor
			agregado = agregado +1
		i = i+1

	imprimirValores(points)

	return points	



#Clasificacion de los puntos en digitales y analogicos
# print("*********************************************************************\n\
# Puntos digitales:")
#Identificacion de los puntos digitales 
def busquedaPuntosDigitales(puntos):
	

	i = 0
	agregado = 0 #Contador de puntos almacenados 
	digital_points = {} #Diccionario que almacena todos los puntos digitales

	while i<len(puntos):
		valor = galba.retornarConsulta("select point_id,initial_state from digital_point where point_id="+str(puntos[i]))
		
		if len(valor)!=0:  #verficacion para validar resultado vacio
			digital_points[agregado] = valor
			agregado = agregado+1	
		i = i+1

	
	imprimirValores(digital_points)

	return digital_points

# # puntosDigitales = busquedaPuntosDigitales(puntos)
# print("*****************************************************************************************\n\
# estados de los puntos digitales")
# #busqueda de los estados de los puntos digitales

def busquedaEstadosPuntosDigitales(puntosDigitales):
	i=0
	agregado = 0
	estadosPuntos={}

	
	while i<len(puntosDigitales):

		valor = galba.retornarConsulta("select point_id, state_id, bit_partner_state from point_state where point_state.point_id="+\
			str(puntosDigitales[i][0]["point_id"]))
		
		if len(valor)!=0:
			estadosPuntos[agregado] = valor
			agregado = agregado +1
		i = i+1

	imprimirValores(estadosPuntos)
	return estadosPuntos 

# estadosPuntosDigitales = busquedaEstadosPuntosDigitales(puntosDigitales)


# print("*********************************************************************\n\
# Alarmas de los puntos digitales:")

def busquedaAlarmasDigitales(estadosPuntosDigitales):
	i = 0
	agregado = 0
	alarmasDigitales = {}

	while i < len(estadosPuntosDigitales):
		valor = galba.retornarConsulta("select * from digital_alarm where digital_alarm.point_id ="+\
			str(estadosPuntosDigitales[i][0]["point_id"]))

		if len(valor)!=0:
			alarmasDigitales[agregado] = valor
			agregado = agregado +1
		i = i+1

	imprimirValores(alarmasDigitales)
	return alarmasDigitales

# alarmasDigitales = busquedaAlarmasDigitales(estadosPuntosDigitales)
# print("***********************************************************************\n\
# repositorio de alarmas digitales:")

def busquedaAlarmasDigitalesAnalogicasRepositorio(alarmasDigitalesAnalogicas):
	i = 0
	j = 0
	agregado = 0
	alarmas = {}

	while i < len(alarmasDigitalesAnalogicas):
		while j< len(alarmasDigitalesAnalogicas[i]):
			valor = galba.retornarConsulta("select alarm_id, severity_id, priority, is_inhibited_alarm, alarm_description, \
			active,is_enabled from alarm where alarm.alarm_id ="+str(alarmasDigitalesAnalogicas[i][j]["alarm_id"]))
			j =j+1
			
			if len(valor)!=0:	
				alarmas[agregado]= valor
				agregado = agregado + 1
		
		i = i+1
		j=0
	
	imprimirValores(alarmas)
	return alarmas

# repositorioAlarmasDigitales =busquedaAlarmasDigitalesAnalogicasRepositorio(alarmasDigitales)





# print("//////////////////////////////////////////////////////////////////////////////////////////////////////////\n\
# Puntos analogicos:")


# Identificacion de los puntos digitales 
def busquedaPuntosAnalogicos(puntos):
	
	i = 0
	agregado = 0
	puntosAnalogicos = {} #Diccionario que almacena todos los puntos analogicos

	while i<len(puntos):
		valor =galba.retornarConsulta("select point_id,in_upper_limit_egu,in_lower_limit_egu,units_in_name\
		 from analog_point where point_id="+str(puntos[i])) 
		
		if len(valor)!=0:
			puntosAnalogicos[agregado] = valor
			agregado = agregado +1	
		i = i+1

	imprimirValores(puntosAnalogicos)
	return puntosAnalogicos

# puntosAnalogicos = busquedaPuntosAnalogicos(puntos)

# print("**********************************************************************\n\
# alarmas Analogicas:")

#Busqueda de las alarmas digitales
def busquedaAlarmasAnalogicas(puntosAnalogicos):
	i = 0
	agregado = 0
	alarmasAnalogicas = {}

	while i < len(puntosAnalogicos):
		valor = galba.retornarConsulta("select alarm_id,alarm_type_id,point_id,numeric_value \
			from analog_alarm where analog_alarm.point_id="+str(puntosAnalogicos[i][0]["point_id"]))
		
		if len(valor)!=0:
			alarmasAnalogicas[agregado] = valor
			agregado = agregado +1
		i= i+1

	imprimirValores(alarmasAnalogicas)
	return alarmasAnalogicas

# alarmasAnalogicas = busquedaAlarmasAnalogicas(puntosAnalogicos)

# print("************************************************************************\n\
# Repositorio de alarmas analogicas")

# repositorioAlarmasAnalogicas =busquedaAlarmasDigitalesAnalogicasRepositorio(alarmasAnalogicas)




