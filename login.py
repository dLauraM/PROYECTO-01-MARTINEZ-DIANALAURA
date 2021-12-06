# Enviamos los datos de usuario a un archivo separado
from login_data import user_data

def login():
				# Solicitamos nombre del usuario
				print("Dame tu nombre de usuario")
				user = input()
				# Solicitamos password del usuario
				print("Ingresa tu contraseña")
				password = input()
				# Inicializamos variable para recorrer la lista de datos del usuario
				index = 0
				# Creamos un bucle para recorrer todas las credenciales en la lista
				while index < len(user_data):
				# Colocamos un if para evaluar si el usuario y contraseña existen
						if user_data[index][0] == user and user_data[index][1] == password:
										# Desplegamos mensaje de bienvenida
										print("Bienvenido al sistema de reportes de Life Store")
										# Regresamos un valor para poder iniciar sesión
										return True
				# Aumentamos la variable para buscar en el siguiente elemento de la lista
						index += 1
				# Desplegamos mensaje de error y devolvemos valor para evitar el ingreso al menu
				print("El usuario o la contraseña no son validos, ingrese credenciales validas")
				return False
