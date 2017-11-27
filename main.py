from conexionDB import conexionDB
from datetime import datetime

galba = conexionDB()
galba.parametrosConexion("prueba","postgres","root","localhost")
galba.conectar()

# lista = ({"cedula":"23468856","nombre":"alfredo"},
# 	{"cedula":"248756","nombre":"alfredo"},
# 	{"cedula":"2487567","nombre":"alfredo"})

# galba.insertarUno("insert into persona (cedula,nombre,apellido) values(%s,%s,%s)",("23468856","alfredo","apellido"))
# galba.actualizar("update persona set nombre = %s where cedula = %s",("luis","23468856"))
# galba.borrar("delete from persona where nombre =%s",("luis",))
# galba.insertarVarios("insert into persona (cedula,nombre) values (%(cedula)s,%(nombre)s)",lista)

# punto = {"punto_id":"2315685","nombre_etiqueta":"hola","descripcion_punto":"none","id_tipo_data":"1","id_procesos_planta":"1"\
# ,"calidad_dato":"buena"},{"punto_id":"2315687","nombre_etiqueta":"hola","descripcion_punto":"none","id_tipo_data":"1","id_procesos_planta":"1"\
# ,"calidad_dato":"buena"}

# print(type(punto[0]))

# punto[0].setdefault("fuente","times_new") #permite ingresar un nuevo elemento al diccionario con su clave

# print(punto[1].keys())
# diccionario = galba.insertarUno("insert into punto (id_punto,nombre_etiqueta,descripcion_punto,id_tipo_data\
# 	,id_procesos_planta,calidad_dato) values (%(punto_id)s,%(nombre_etiqueta)s,%(descripcion_punto)s,%(id_tipo_data)s\
# 	,%(id_procesos_planta)s,%(calidad_dato)s)",punto)

# galba.mostrarConsulta("select insertar_persona('2368856','luis','mendoza')")
# galba.mostrarConsulta("select borrar_tabla()");
# fecha = datetime.now()
# print(type(fecha))

galba.cerrarConexion()