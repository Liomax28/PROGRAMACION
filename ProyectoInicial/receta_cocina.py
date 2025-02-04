# Receta de cocina 

print("*** Receta de Cocina ***")

#Valores que se van a introducir 
nombre_receta = input("\nIntroduce el nombre de la receta: ")
ingredientes = input("Introduce los ingredientes: ")
tiempo_preparacion = int(input("Introduce el timepo de preparacion(En minutos): "))
dificultad = input("Introduce la dificultad de la receta(Facil, Media, Dificil): ")

#Imprimir la receta
print("--------------------------------------------------------------")
print(f"Nombre de la receta: {nombre_receta}")
print(f"Ingredientes que contiene: {ingredientes}")
print(f"Tiempo de preparcion: {tiempo_preparacion}")
print(f"Dificultad: {dificultad}")