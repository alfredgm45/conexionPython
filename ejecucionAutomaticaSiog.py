from conexionDB import conexionDB
import conexionServidor as servidor
import insercionBDSiog as insercion




siog = conexionDB()
siog.parametrosConexion("siog","postgres","root","localhost")
siog.conectar()

plantas = siog.retornarConsulta("select * from planta")

while True:
	
	i=0 
	while i < len(plantas):
		print(plantas[i]['id_planta']+'  '+plantas[i]['ip_planta']+' ejecutando conexion Servidor......')
		# servidor.conectarServidorAdquisicionData(plantas[i]['ip_planta'],plantas[i]['id_planta'])
		print(plantas[i]['id_planta']+'  '+plantas[i]['ip_planta']+' ejecutadando insercion de datos a la base de datos........')
		# insercion.insercionPuntosSiog(plantas[i]['id_planta'],plantas[i]['ip_planta'])
		

		print(str(i))
		i = i + 1