#Sistema de Empleados 
print("*** Sistema de Empleados ***")

#Pedir los valores en consola
nombre_empleado = input("\nNombre del empleado: ")
edad_empleado = int(input("Edad del empleado: "))
salario_empleado = float(input("Salario del empleado: "))
jefe_departamento = input("Es jefe de departamento (Si/No)? ")

#comvertir a un tipo bool si la variable jefe_departamento
jefe_departamento = jefe_departamento.lower() == "si"

#Imprimir los calores del Empleado
print("\nDatos del Empleado")
print(f"Nombre: {nombre_empleado}")
print(f"Edad: {edad_empleado}")
print(f"Salario: {salario_empleado: .2f}")
print(f"Es jefe de departamento? {jefe_departamento}")
