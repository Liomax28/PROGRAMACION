# Generador de Email con entrada de datos
print("*** Generador de Email ***")

# Entrada de datos desde la consola y variables
nombre_usuario = input("\nCuales son sus nombres? ")
apellido_usuario = input("Cuales son sus apellidos? ")
nombre_empresa = input("Cual es el nombre de la empresa? ")
dominio = input("Cual es el dominio de su empres? ")

# Datos normalizados
usuario_normalizado = nombre_usuario.strip().lower().replace(" ", ".")
apellido_normalizado = apellido_usuario.strip().lower().replace(" ", ".")
empresa_normalizada = nombre_empresa.strip().lower().replace(" ", "")
dominio_normalizado = dominio.strip().lower().replace(" ", "")
# Generar Email 
Email = f"{usuario_normalizado}.{apellido_normalizado}@{empresa_normalizada}{dominio_normalizado}"

# Impresion en pantalla 
print(f''' 
        Tu nueva direccion de correo generado por el sistema es: 
        {Email}
        Felicidades!
        ''')

