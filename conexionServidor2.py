import paramiko
import os
import sys

#inicia un cliente ssh
ssh_client = paramiko.SSHClient()


#establecer politica por defectos para localizar las llaves del host localmente
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#conectarse
ssh_client.connect(sys.argv[1],22,'galba','galba')

#Ejecutar un comando de forma remota capturando entrada, salida y error estandar 
entrada, salida , error = ssh_client.exec_command('cd /home/galba/Documentos;mkdir pythonData;cd pythonData/;touch hola.txt;ls')
#Mostrar la salida estandar en pantalla
for i in salida:
	print(i)

#creacion del objeto sftp para la transmision del archivo
sftp = ssh_client.open_sftp()

#verificando si el directorio ya esta creado
if os.path.isdir("/home/alfredo/Documentos/conexionPython/galbaData/taej")==False:
	
	os.system("cd /home/alfredo/Documentos/;chmod -R 777 conexionPython;cd conexionPython/;mkdir galbaData;cd galbaData;mkdir taej")

rutaRemota = "/home/galba/Documentos/pythonData/hola.txt"

rutaLocal = "/home/alfredo/Documentos/conexionPython/galbaData/taej/hola.txt"

sftp.get(rutaRemota,rutaLocal)




# Cerra la conexion
sftp.close()
ssh_client.close()