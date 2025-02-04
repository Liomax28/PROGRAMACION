# Generador de ID para usuarios
# Importar el modulo random
from random import randint

print("*** Sistema Generador de ID Unico ***")

# Valores que se van a introducir desde la consola 
nombre_usuario = input("\nCual es su Nombre? ")
apellido_usuario = input("Cual es su Apellido? ")
nacimiento = input("Cual es su año de nacimiento? ")

# Datos normalizados
nombre_mayusculas = nombre_usuario[0:2].upper().strip()
apellido_mayusculas = apellido_usuario.upper().strip()[0:2]
nacimiento_digitos = nacimiento.strip()[2:4] #Tambien puede ser [2:]

# Generar 4 valiores aleatorios 
numero_aleatorio = randint(1000,9999)

#Generar la ID
ID_usuario = f"{nombre_mayusculas}{apellido_mayusculas}{nacimiento_digitos}{numero_aleatorio}"

# Imprimir el ID

print(f"\nHola {nombre_usuario}")
print(f'''\tTu numero de identificacion (ID) generado por el sistema es: \n\t{ID_usuario}\n\tFelicidades!''')


print(f'''\nHola {nombre_usuario}Tu numero de identificacion (ID) generado por el sistema es: 
      {ID_usuario}
      tFelicidades! ''')