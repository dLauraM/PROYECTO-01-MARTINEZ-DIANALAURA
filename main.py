# Importamos la libreria pandas para apoyarnos a manejar los datos
import pandas
# Separamos el login de las funciones principales
from login import login
# Importamos las listas de datos de productos
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

# Configuramos pandas para que nos muestre todas las columnas en los print
pandas.set_option("display.max_rows", None, "display.max_columns", None)
isLogin = True

# Función que calcula los productos más vendidos
def best_sellers():
				print("A continuación podrá consultar los 5 productos más vendidos")
				# Generamos los dataset para lifestore_sales y lifestore_products
				sales_list = pandas.DataFrame(lifestore_sales)
				product_list = pandas.DataFrame(lifestore_products)
				# Obtenemos los resultados de el conteo de productos más vendidos y de esos obtenemos los últimos 5
				product_count = sales_list[1].value_counts()[:5]
				print(product_count)
				print("La descripción de los productos se encuentra a continuación")
				# Obtenemos los indices de la lista anterior para poder encontrar los productos en la lista lifestore_products
				index = product_count.index
				# Restamos 1 a toda la lista de indices de productos más vendidos para que coincidan con los indices de la lista lifestore_products
				index = index - 1
				print(product_list.iloc[index])

# Función que calcula los productos menos vendidos
def weak_products():
				print("A continuación podrá consultar los 5 productos menos vendidos")
				# Generamos los dataset para lifestore_sales y lifestore_products
				sales_list = pandas.DataFrame(lifestore_sales)
				product_list = pandas.DataFrame(lifestore_products)
				# Obtenemos los resultados de el conteo de productos menos vendidos y de esos obtenemos los últimos 5
				product_count = sales_list[1].value_counts().iloc[::-1]
				print(product_count[:5])
				print("La descripción de los productos se encuentra a continuación")
				# Obtenemos los indices de la lista anterior para poder encontrar los productos en la lista lifestore_products
				index = product_count[:5].index
				# Restamos 1 a toda la lista de indices de productos menos vendidos para que coincidan con los indices de la lista lifestore_products
				index = index - 1
				print(product_list.iloc[index])

# Función que calcula los productos más buscados
def major_search():
				print("A continuación podrá consultar los 10 productos más buscados")
				# Generamos los dataset para lifestore_searches y lifestore_products
				search_list = pandas.DataFrame(lifestore_searches)
				product_list = pandas.DataFrame(lifestore_products)
				# Obtenemos los resultados de el conteo de productos más vendidos y de esos obtenemos los últimos 5
				search_count = search_list[1].value_counts()[:10]
				print(search_count)
				print("La descripción de los productos se encuentra a continuación")
				# Obtenemos los indices de la lista anterior para poder encontrar los productos en la lista lifestore_products
				index = search_count.index
				# Restamos 1 a toda la lista de indices de productos más buscados para que coincidan con los indices de la lista lifestore_products
				index = index - 1
				print(product_list.iloc[index])

# Función que calcula los productos menos vendidos
def minor_search():
				print("A continuación podrá consultar los 10 productos menos buscados")
				# Generamos los dataset para lifestore_searches y lifestore_products
				search_list = pandas.DataFrame(lifestore_searches)
				product_list = pandas.DataFrame(lifestore_products)
				# Obtenemos los resultados de el conteo de productos más vendidos y de esos obtenemos los últimos 5
				search_count = search_list[1].value_counts().iloc[::-1]
				print(search_count[:10])
				print("La descripción de los productos se encuentra a continuación")
				# Obtenemos los indices de la lista anterior para poder encontrar los productos en la lista lifestore_products
				index = search_count[:10].index
				# Restamos 1 a toda la lista de indices de productos menos buscados para que coincidan con los indices de la lista lifestore_products
				index = index - 1
				print(product_list.iloc[index])

# Función que calcula los productos mejor rankeados
def best_score():
				print("A continuación podrá consultar los 5 productos con mejores reseñas")
				# Generamos los dataset para lifestore_sales y lifestore_products
				score_list = pandas.DataFrame(lifestore_sales)
				product_list = pandas.DataFrame(lifestore_products)
				# Obtenemos los resultados de el conteo de productos mejor reseñados y de esos obtenemos los últimos 5
				average = score_list.groupby(1).mean()
				print(average.sort_values(2, ascending=False)[:5])
				print("La descripción de los productos se encuentra a continuación")
				# Obtenemos los indices de la lista anterior para poder encontrar los productos en la lista lifestore_products
				index = average.sort_values(2, ascending=False)[:5].index
				# Restamos 1 a toda la lista de indices de productos mejor reseñados para que coincidan con los indices de la lista lifestore_products
				index = index - 1
				print(product_list.iloc[index])

# Función que calcula los productos peor rankeados
def worst_score():
				print("A continuación podrá consultar los 5 productos con peores reseñas (revise columna '2')")
				# Generamos los dataset para lifestore_sales y lifestore_products
				score_list = pandas.DataFrame(lifestore_sales)
				product_list = pandas.DataFrame(lifestore_products)
				# Obtenemos los resultados de el conteo de productos peores reseñados y de esos obtenemos los últimos 5
				average = score_list.groupby(1).mean()
				print(average.sort_values(2, ascending=True)[:5])
				print("La descripción de los productos se encuentra a continuación")
				# Obtenemos los indices de la lista anterior para poder encontrar los productos en la lista lifestore_products
				index = average.sort_values(2, ascending=True)[:5].index
				# Restamos 1 a toda la lista de indices de productos peores reseñados para que coincidan con los indices de la lista lifestore_products
				index = index - 1
				print(product_list.iloc[index])

# Función que calcula el total de ganancias
def total_earnings():
				print("Reporte de ganancias")
				# Generamos los dataset para lifestore_searches y lifestore_products
				search_list = pandas.DataFrame(lifestore_searches)
				product_list = pandas.DataFrame(lifestore_products)
				# Obtenemos los resultados de el conteo de productos más vendidos y de esos obtenemos los últimos 5
				search_count = search_list[1].value_counts().sort_index(ascending=True)
				print(search_count.reset_index(drop=True))
				print("La descripción de los productos se encuentra a continuación")
				# Obtenemos los indices de la lista anterior para poder encontrar los productos en la lista lifestore_products
				earnings = search_count.reset_index(drop=True)*product_list[2]
				print("$",f'{earnings.dropna().sum():,}')


# Función muestra el menú para los reportes de ventas
def sales_menu():
				continueWhile = True
				while continueWhile:
								# Mostramos menú del reporte de ventas
								print("Seleccione una opción para obtener un reporte de ventas")
								print("1. Total de ingresos historico")
								print("2. Ventas promedio mensuales")
								print("3. Ventas totales anuales")
								print("4. Meses con más ventas al año")
								print("5. Regresar al menú anterior")
								print("6. Salir")
								print("Ingrese el número de la opción deseada")
								opcion_menu = int(input())

								# Colocamos un if para cada caso incluyendo las excepciones
								if opcion_menu == 1:
												total_earnings()
								elif opcion_menu == 2:
												print("opc")
								elif opcion_menu == 3:
												print("opc")
								elif opcion_menu == 4:
												print("opc")
								elif opcion_menu == 5:
												main()
												return True
								elif opcion_menu == 6:
												return False
								else:
												print("Opción no valida, selecciones una opción del menú")

def main():
				if login() and isLogin:
								continueWhile = True
								while continueWhile:
												# Mostramos menú del sistema
												print("A continuación se muestran las opcioones del menú")
												print("1. Productos con mayores ventas y mayores búsquedas")
												print("2. Productos con menores ventas y menores búsquedas")
												print("3. Productos con mejores y peores reseñas")
												print("4. Reporte de ventas")
												print("5. Salir")
												# Solicitamos que el usuario seleccione una opción
												print("Ingrese el número de la opción deseada")
												opcion_menu = int(input())

												# Colocamos un if para cada caso incluyendo las excepciones
												if opcion_menu == 1:
																best_sellers()
																major_search()
												elif opcion_menu == 2:
																weak_products()
																minor_search()
												elif opcion_menu == 3:
																best_score()
																worst_score()
												elif opcion_menu == 4:
																if not sales_menu():
																				continueWhile = False
												elif opcion_menu == 5:
																continueWhile = False
												else:
																print("Opción no valida, selecciones una opción del menú")
								return 0

if __name__ == "__main__":
    main()