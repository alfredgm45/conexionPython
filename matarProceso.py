import subprocess 
import sys

#obtengo el proceso del script que ejecuta la adquisicion de los datos
proceso= str(subprocess.check_output("ps a | grep "+sys.argv[1], shell=True))

salida = proceso.lstrip("b'")
# print(salida)
salida= salida.split(" ")

print(salida[1]) 
#proceso[0] contiene el PID del proceso el cual se utiliza para matar posteriormente dicho proceso 


subprocess.check_output("kill "+salida[1], shell = True)




