from conexionDB import conexionDB
import busquedaBdGalba as buscador
import lecturaEntradaPuntosJson as lectorEntradaPunto
import adquisicionHtml as html
from datetime import datetime
# conexion a la  base de datos GALBA (servidor mirrow)
siog = conexionDB()
siog.parametrosConexion("siog","postgres","root","localhost")
siog.conectar()




entradaPuntos = lectorEntradaPunto.retornarArregloJsonPtyhon("taecjaa")
print(str(entradaPuntos))

def validacionEntradaPuntos(idPuntos, procesos):
	i = 0
	
	print(str(len(idPuntos)))
	while i<len(idPuntos):	
		print(idPuntos[i])
		if idPuntos[i]=='-' or procesos[i]=='-':

			return -1
		else:
			return 1
		i = i+1

print(str(validacionEntradaPuntos(entradaPuntos["point_id"],entradaPuntos["id_proceso"])))	
		
# 		
# buscador.imprimirValores(entradaPuntos)
if validacionEntradaPuntos(entradaPuntos["point_id"],entradaPuntos["id_proceso"])==1:
	
	print("***********************************************************************\n\
	Puntos ingresados por administrador Operativo")
	points = buscador.busquedaPuntos(entradaPuntos["point_id"])


	#busca las coordenadas(donde se ubican en el arreglo) de los puntos analogicos o digitales en el repositorio de los puntos
	def retornarCoordenadas(puntos,tipoPuntos):
		i = 0
		j= 0
		
		c = []
		
		while i<len(tipoPuntos):
			while j<len(puntos):
				if tipoPuntos[i][0]["point_id"]==puntos[j][0]["point_id"]:
					c.append(j)
					
				j = j+1 
			
			i = i+1
			j= 0

		return c


	print("*********************************************************************\n\
	Puntos digitales:")
	puntosDigitales = buscador.busquedaPuntosDigitales(entradaPuntos["point_id"]);


	print("*****************************************************************************************\n\
	estados de los puntos digitales")
	estadosPuntosDigitales = buscador.busquedaEstadosPuntosDigitales(puntosDigitales)

	print("*********************************************************************\n\
	Alarmas de los puntos digitales:")

	alarmasDigitales = buscador.busquedaAlarmasDigitales(estadosPuntosDigitales)

	print("***********************************************************************\n\
	repositorio de alarmas digitales:")

	repositorioAlarmasDigitales = buscador.busquedaAlarmasDigitalesAnalogicasRepositorio(alarmasDigitales)

	print("//////////////////////////////////////////////////////////////////////////////////////////////////////////\n\
	Puntos analogicos:")

	puntosAnalogicos = buscador.busquedaPuntosAnalogicos(entradaPuntos["point_id"])

	print("**********************************************************************\n\
	alarmas Analogicas:")

	alarmasAnalogicas = buscador.busquedaAlarmasAnalogicas(puntosAnalogicos);

	print("************************************************************************\n\
	Repositorio de alarmas analogicas")

	repositorioAlarmasAnalogicas = buscador.busquedaAlarmasDigitalesAnalogicasRepositorio(alarmasAnalogicas)

	buscador.galba.cerrarConexion()


	coordenadasD = retornarCoordenadas(points,puntosDigitales)

	if len(coordenadasD)>0:
		calidadesD = html.retornarCalidadPuntoDigital("taecjaa",points,coordenadasD)
		estadosD = html.retornarEstadoPuntoDigital("taecjaa",points, coordenadasD)
	else:
		print("no hay puntos digitales")


	coordenadasA = retornarCoordenadas(points,puntosAnalogicos)

	if len(coordenadasA)>0:
		calidadesA=html.retornarCalidadPuntoAnalogico("taecjaa",points,coordenadasA)
		valoresA = html.retornarValorPuntoAnalogico("taecjaa", points , coordenadasA)
	else:
		print("no hay puntos analogicos")



	buscador.imprimirValores(coordenadasA)
	buscador.imprimirValores(coordenadasD)


	# buscador.imprimirValores(calidadesA)
	# buscador.imprimirValores(calidadesD)
	# buscador.imprimirValores(valoresA)
	# buscador.imprimirValores(estadosD)

	#///////////////////////////////////////////////////////////////////////////////////////////////////////
	#verificaion de los puntos, digitales/analogicos, alarmas, alarmas digitales/analogicas, estados de los puntos digitales
	#Y los estados de las alarmas digitales
	def verificacionPuntos(punto):
		
		point = siog.retornarConsulta("select id_punto from punto where id_punto="+str(punto))

		if len(point)>0:
			return True
		else:
			return False 

	def verificacionPuntoDigital(punto):
		point = siog.retornarConsulta("select id_punto from punto_digital where id_punto="+str(punto))

		if len(point)>0:
			return True
		else:
			return False 
		

	def verificacionEstadoPuntoDigital(idPunto,idEstado):
		
		estadoPuntoDigital = siog.retornarConsulta("select id_punto from estado_punto where id_punto="+str(idPunto)+" and id_estado="+str(idEstado))

		if len(estadoPuntoDigital)>0:
			return True
		else:
			return False

	def verificacionAlarmaDigital(idAlarma,idPunto,idEstado):
		
		alarmaDigital = siog.retornarConsulta("select id_punto from alarma_digital where id_alarma= "+str(idAlarma)+" and id_punto="\
			+str(idPunto)+" and id_estado="+str(idEstado))

		if len(alarmaDigital)>0:
			return True	
		else:
			return False

	def verificacionPuntoAnalogico(punto):
		point = siog.retornarConsulta("select id_punto from punto_analogico where id_punto="+str(punto))

		if len(point)>0:
			return True
		else:
			return False 

	def verificacionAlarmaAnalogica(idAlarma,idPunto,idTipoAlarma):
		
		alarmaAnalogica = siog.retornarConsulta("select id_alarma from alarma_analogica where id_alarma="+str(idAlarma)+" and\
			id_tipo_alarma="+str(idTipoAlarma)+" and id_punto="+str(idPunto))

		if len(alarmaAnalogica)>0:
			return True
		else:
			return False
		


	def verificacionRepositorioAlarma(idAlarma):
		
		alarma = siog.retornarConsulta("select id_alarma from alarma where id_alarma="+str(idAlarma))

		if len(alarma)>0:
			return True
		else:
			return False

	# Fin de toda la verificacion para la validacion de la adquisicion de SIOG
	# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
		
		

	def insercionPuntos(puntos,coordA,coordD,calidA,calidD,proceso):
		i = 0
		j = 0
		z = 0
		

		while i<len(puntos):
			if i==coordA[j]:
				if verificacionPuntos(puntos[i][0]["point_id"])==False:
					fecha1 =datetime.now()
					siog.insertarUno("insert into punto(id_punto,nombre_etiqueta,descripcion_punto,id_tipo_data,\
					id_procesos_planta,calidad_dato,fecha_insercion_punto,fecha_modificacion_punto) \
				    values(%s,%s,%s,%s,%s,%s,%s,%s)",(puntos[i][0]["point_id"],puntos[i][0]["tag_name"],puntos[i][0]["point_description"],\
				    puntos[i][0]["data_type_id"],proceso["id_proceso"][i],calidA[j],fecha1,fecha1))
					if j < len(coordA)-1:
					
						j = j+1
				else:
					fecha2 = datetime.now()
					siog.actualizar("update punto set nombre_etiqueta=%s, descripcion_punto=%s, id_tipo_data=%s, \
					calidad_dato=%s, fecha_modificacion_punto=%s where\
					id_punto=%s",(puntos[i][0]["tag_name"],puntos[i][0]["point_description"],puntos[i][0]["data_type_id"],\
				    calidA[j],fecha2,puntos[i][0]["point_id"]))
					
					if j < len(coordA)-1:
					
						j = j+1
				

			if i==coordD[z]:
				 
				 if verificacionPuntos(puntos[i][0]["point_id"])==False:
				 	fecha3 = datetime.now()
				 	siog.insertarUno("insert into punto(id_punto,nombre_etiqueta,descripcion_punto,id_tipo_data\
				 	,id_procesos_planta,calidad_dato,fecha_insercion_punto,fecha_modificacion_punto) \
				     values(%s,%s,%s,%s,%s,%s,%s,%s)",(puntos[i][0]["point_id"],puntos[i][0]["tag_name"],puntos[i][0]["point_description"],\
				     puntos[i][0]["data_type_id"],proceso["id_proceso"][i],calidD[z],fecha3,fecha3))

				 	if z < len(coordD)-1:
				 		z = z + 1
				 else:
				 	fecha4 = datetime.now()
				 	
				 	siog.actualizar("update punto set nombre_etiqueta=%s, descripcion_punto=%s, id_tipo_data=%s, \
				 	calidad_dato=%s, fecha_modificacion_punto=%s where\
					id_punto=%s",(puntos[i][0]["tag_name"],puntos[i][0]["point_description"],puntos[i][0]["data_type_id"],\
					calidD[z],fecha4,puntos[i][0]["point_id"]))

				 	if z < len(coordD)-1:
				 		z = z + 1


			i = i + 1

	def insercionPuntosSinDigitales(puntos,coordA,calidA,proceso):
		i = 0
		j = 0
		while i<len(puntos):
			if i==coordA[j]:
				if verificacionPuntos(puntos[i][0]["point_id"])==False:
					fecha1 =datetime.now()
					siog.insertarUno("insert into punto(id_punto,nombre_etiqueta,descripcion_punto,id_tipo_data,\
					id_procesos_planta,calidad_dato,fecha_insercion_punto,fecha_modificacion_punto) \
				    values(%s,%s,%s,%s,%s,%s,%s,%s)",(puntos[i][0]["point_id"],puntos[i][0]["tag_name"],puntos[i][0]["point_description"],\
				    puntos[i][0]["data_type_id"],proceso["id_proceso"][i],calidA[j],fecha1,fecha1))
					if j < len(coordA)-1:
					
						j = j+1
				else:
					fecha2 = datetime.now()
					siog.actualizar("update punto set nombre_etiqueta=%s, descripcion_punto=%s, id_tipo_data=%s, \
					calidad_dato=%s, fecha_modificacion_punto=%s where\
					id_punto=%s",(puntos[i][0]["tag_name"],puntos[i][0]["point_description"],puntos[i][0]["data_type_id"],\
				    calidA[j],fecha2,puntos[i][0]["point_id"]))
					
					if j < len(coordA)-1:
					
						j = j+1


			i = i + 1

	def insercionPuntosSinAnalogicos(puntos,coordD,calidD,proceso):
		i = 0
		z = 0
		if i==coordD[z]:
				 
			 if verificacionPuntos(puntos[i][0]["point_id"])==False:
			 	fecha3 = datetime.now()
			 	siog.insertarUno("insert into punto(id_punto,nombre_etiqueta,descripcion_punto,id_tipo_data\
			 	,id_procesos_planta,calidad_dato,fecha_insercion_punto,fecha_modificacion_punto) \
			     values(%s,%s,%s,%s,%s,%s,%s,%s)",(puntos[i][0]["point_id"],puntos[i][0]["tag_name"],puntos[i][0]["point_description"],\
			     puntos[i][0]["data_type_id"],proceso["id_proceso"][i],calidD[z],fecha3,fecha3))

			 	if z < len(coordD)-1:
			 		z = z + 1
			 else:
			 	fecha4 = datetime.now()
			 	
			 	siog.actualizar("update punto set nombre_etiqueta=%s, descripcion_punto=%s, id_tipo_data=%s, \
			 	calidad_dato=%s, fecha_modificacion_punto=%s where\
				id_punto=%s",(puntos[i][0]["tag_name"],puntos[i][0]["point_description"],puntos[i][0]["data_type_id"],\
				calidD[z],fecha4,puntos[i][0]["point_id"]))

			 	if z < len(coordD)-1:
			 		z = z + 1

	def insercionPuntosDigitales(puntosD,estadosR):
		i = 0

		while i < len(puntosD):
			if verificacionPuntoDigital(puntosD[i][0]["point_id"])==False:
				
				siog.insertarUno("insert into punto_digital(id_punto,estado_inicial,estado_recolectado) \
					values (%s,%s,%s)",(puntosD[i][0]["point_id"],puntosD[i][0]["initial_state"],estadosR[i]))

				i = i + 1
			else:
				siog.actualizar("update punto_digital set estado_inicial=%s, estado_recolectado=%s where id_punto=%s",
					(puntosD[i][0]["initial_state"],estadosR[i],puntosD[i][0]["point_id"]))
				i = i + 1

	def insercionEstadosDigitales(estados):
		i = 0
		j = 0
		while i < len(estados):
			
			while j < len(estados[i]):
				if verificacionEstadoPuntoDigital(estados[i][j]["point_id"],estados[i][j]["state_id"])==False:
					
					siog.insertarUno("insert into estado_punto(id_punto,id_estado,bit_asoc_estado) values(%s,%s,%s)",\
						(estados[i][j]["point_id"],estados[i][j]["state_id"],estados[i][j]["bit_partner_state"]))
					j = j+1
				else:
					siog.actualizar("update estado_punto set bit_asoc_estado=%s where id_punto=%s and id_estado=%s",\
					(estados[i][j]["bit_partner_state"],estados[i][j]["point_id"],estados[i][j]["state_id"]))
					j = j + 1
				
			j = 0
			i = i + 1

	def insercionAlarmasDigitalesAnalogicasRepositorio(alarmas,tipoAlarmas):
		i = 0 
		j = 0
		k = 0
		while i < len(tipoAlarmas):
			while j < len(tipoAlarmas[i]):
				if alarmas[k][0]["alarm_id"]==tipoAlarmas[i][j]["alarm_id"]:
					if verificacionRepositorioAlarma(alarmas[k][0]["alarm_id"])==False:
						
						siog.insertarUno("insert into alarma(id_alarma,id_severidad,prioridad,esta_alarma_inhibida,descripcion_alarma,activa,esta_disponible,id_punto) \
						values(%s,%s,%s,%s,%s,%s,%s,%s)",(alarmas[k][0]["alarm_id"],alarmas[k][0]["severity_id"],alarmas[k][0]["priority"],alarmas[k][0]["is_inhibited_alarm"],\
						alarmas[k][0]["alarm_description"],alarmas[k][0]["active"],alarmas[k][0]["is_enabled"],tipoAlarmas[i][j]["point_id"]))
					else:
						siog.actualizar("update alarma set id_severidad=%s, prioridad=%s, esta_alarma_inhibida=%s,\
						descripcion_alarma=%s, activa=%s, esta_disponible=%s where id_alarma=%s",(alarmas[k][0]["severity_id"],\
						alarmas[k][0]["priority"],alarmas[k][0]["is_inhibited_alarm"],alarmas[k][0]["alarm_description"],\
						alarmas[k][0]["active"],alarmas[k][0]["is_enabled"],alarmas[k][0]["alarm_id"]))
					
				
				k= k + 1
				j = j + 1
			j = 0
			
			

			i = i +1

	def insercionAlarmasDigitales(alarmasDigitales):
		i = 0
		j = 0
		while i < len(alarmasDigitales):
			
			while j < len(alarmasDigitales[i]):
				if verificacionAlarmaDigital(alarmasDigitales[i][j]["alarm_id"],alarmasDigitales[i][j]["point_id"],\
					alarmasDigitales[i][j]["state_id"])==False:
					
					siog.insertarUno("insert into alarma_digital(id_alarma,id_punto,id_estado,bit_estado_aso_alarma,id_tipo_alarma) \
						values(%s,%s,%s,%s,%s)",(alarmasDigitales[i][j]["alarm_id"],alarmasDigitales[i][j]["point_id"],\
						alarmasDigitales[i][j]["state_id"],alarmasDigitales[i][j]["bit_partner_alarm"],\
						alarmasDigitales[i][j]["alarm_type_id"]))
					j = j+1
				else:
					
					siog.actualizar("update alarma_digital set bit_estado_aso_alarma=%s, id_tipo_alarma=%s where id_alarma=%s and \
					id_punto=%s and id_estado = %s",(alarmasDigitales[i][j]["bit_partner_alarm"],alarmasDigitales[i][j]["alarm_type_id"]\
					,alarmasDigitales[i][j]["alarm_id"],alarmasDigitales[i][j]["point_id"],alarmasDigitales[i][j]["state_id"]))
					j = j + 1
				

			j = 0
			i = i + 1




	def insercionPuntosAnalogicos(puntosA,valoresA):
		i = 0

		while i < len(puntosA):
			if verificacionPuntoAnalogico(puntosA[i][0]["point_id"])==False:
				
				siog.insertarUno("insert into punto_analogico(id_punto,lim_sup_ent_punto,lim_inf_ent_punto,unid_entrada_inge,\
					valor_recolectado) values (%s,%s,%s,%s,%s)",(puntosA[i][0]["point_id"],puntosA[i][0]["in_upper_limit_egu"]\
					,puntosA[i][0]["in_lower_limit_egu"],puntosA[i][0]["units_in_name"],valoresA[i]))

				i = i + 1
			else:
				siog.actualizar("update punto_analogico set lim_sup_ent_punto=%s, lim_inf_ent_punto=%s , unid_entrada_inge=%s,\
					valor_recolectado=%s where id_punto=%s",(puntosA[i][0]["in_upper_limit_egu"],puntosA[i][0]["in_lower_limit_egu"]\
				,puntosA[i][0]["units_in_name"],valoresA[i],puntosA[i][0]["point_id"]))

				i = i + 1
			






	def insercionAlarmasAnalogicas(alarmasAnalogicas):
		i = 0
		j = 0 

		while i < len(alarmasAnalogicas):
			
			while j < len(alarmasAnalogicas[i]):
				if verificacionAlarmaAnalogica(alarmasAnalogicas[i][j]["alarm_id"],alarmasAnalogicas[i][j]["point_id"]\
				,alarmasAnalogicas[i][j]["alarm_type_id"])==False:
					
					siog.insertarUno("insert into alarma_analogica(id_alarma,id_tipo_alarma,id_punto,valor_Numerico) \
					values (%s,%s,%s,%s)",(alarmasAnalogicas[i][j]["alarm_id"],alarmasAnalogicas[i][j]["alarm_type_id"],\
					alarmasAnalogicas[i][j]["point_id"],alarmasAnalogicas[i][j]["numeric_value"]))
					
					j = j + 1

				else:

					siog.actualizar("update alarma_analogica set valor_numerico=%s where id_alarma=%s and id_tipo_alarma=%s\
					and id_punto=%s",(alarmasAnalogicas[i][j]["numeric_value"],alarmasAnalogicas[i][j]["alarm_id"]\
					,alarmasAnalogicas[i][j]["alarm_type_id"],alarmasAnalogicas[i][j]["point_id"]))

					j = j + 1
				
			j = 0
			i = i + 1


	if len(coordenadasD)==0:
		insercionPuntosSinDigitales(points,coordenadasA,calidadesA,entradaPuntos)
		insercionPuntosAnalogicos(puntosAnalogicos,valoresA)
		insercionAlarmasDigitalesAnalogicasRepositorio(repositorioAlarmasAnalogicas,alarmasAnalogicas)
		insercionAlarmasAnalogicas(alarmasAnalogicas)

	else:
		if len(coordenadasA)==0:
			insercionPuntosSinAnalogicos(points,coordenadasD,calidadesD,entradaPuntos)
			insercionPuntosDigitales(puntosDigitales,estadosD)
			insercionEstadosDigitales(estadosPuntosDigitales)
			insercionAlarmasDigitalesAnalogicasRepositorio(repositorioAlarmasDigitales,alarmasDigitales)
			insercionAlarmasDigitales(alarmasDigitales)
		else:
			insercionPuntos(points,coordenadasA,coordenadasD,calidadesA,calidadesD,entradaPuntos)
			insercionPuntosDigitales(puntosDigitales,estadosD)
			insercionEstadosDigitales(estadosPuntosDigitales)
			insercionAlarmasDigitalesAnalogicasRepositorio(repositorioAlarmasDigitales,alarmasDigitales)
			insercionAlarmasDigitales(alarmasDigitales)
			insercionAlarmasDigitalesAnalogicasRepositorio(repositorioAlarmasAnalogicas,alarmasAnalogicas)
			insercionPuntosAnalogicos(puntosAnalogicos,valoresA)
			insercionAlarmasAnalogicas(alarmasAnalogicas)

else:
	print('no hay puntos seleccionados o hubo una violacion de una restriccion')







