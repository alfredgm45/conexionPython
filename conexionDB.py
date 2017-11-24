import psycopg2
import psycopg2.extras
import sys

class conexionDB(object):
	"""docstring for ConexionDB"""
	def __init__(self):
		
		self.dbname= None
		self.user = None
		self.password = None
		self.host = None
		self.conexion = None
		self.cursor = None
		self.filas = None

	def getCursor(self):
		return self.cursor
		
	def parametrosConexion(self,dbname,user,password,host):
		self.dbname = dbname
		self.user = user
		self.password = password
		self.host = host 

	def conectar(self):
		self.conexion = psycopg2.connect("dbname="+self.dbname+" user="+self.user+" password="+self.password+" host="+self.host)
		self.cursor = self.conexion.cursor(cursor_factory=psycopg2.extras.DictCursor) #las consultas retornan diccionarios
	
	def insertarUno(self,consulta,parametro):		
	
		self.cursor.execute(consulta,parametro)
		self.conexion.commit()

	def insertarVarios(self,consulta,diccionario):

		self.cursor.executemany(consulta,diccionario)
		self.conexion.commit()


	def mostrarConsulta(self,consulta):

		
		self.cursor.execute(consulta)
		self.filas = self.cursor.fetchall()
		self.conexion.commit()
		for i in self.filas:
			print (i)

	def retornarConsulta(self,consulta):
		
		
		self.cursor.execute(consulta)
		self.filas = self.cursor.fetchall()
		return self.filas

	def actualizar(self,consulta,parametro):

		self.cursor.execute(consulta,parametro)
		self.conexion.commit()

	def borrar(self,consulta,parametro):
		
		self.cursor.execute(consulta,parametro)
		self.conexion.commit()

	def cerrarConexion(self):
		self.cursor.close()
		self.conexion.close()



