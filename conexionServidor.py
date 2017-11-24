import paramiko
import os
import sys

def conectarServidorAdquisicionData(servidor,nombrePlanta):
	
	#inicia un cliente ssh
	ssh_client = paramiko.SSHClient()

	#establecer politica por defectos para localizar las llaves del host localmente
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	#conectarse
	ssh_client.connect(servidor,22,'galba','galba')

	#Ejecutar un comando de forma remota capturando entrada, salida y error estandar 
	entrada, salida , error = ssh_client.exec_command('cd /opt/siog;mkdir '+nombrePlanta+';chmod -R 777 '+nombrePlanta+';cd /opt/siog/'+nombrePlanta+';\
		dst-scada-reportConfiguration')

	#Mostrar la salida estandar en pantalla
	for i in salida:
		print(i)

	# creacion del objeto sftp para la transmision del archivo
	sftp = ssh_client.open_sftp()

	if os.path.isdir("/opt/siog/"+nombrePlanta)==False:
		
		os.system("cd /opt/siog ;mkdir "+nombrePlanta+";chmod -R 777 "+nombrePlanta)


	rutaRemota = "/opt/siog/"+nombrePlanta+"/AcquisitionData.html"

	rutaLocal = "/opt/siog/"+nombrePlanta+"AcquisitionData.html"

	sftp.get(rutaRemota,rutaLocal)

	# Cerra la conexion
	sftp.close()
	ssh_client.close()

