#Generador de Email
'''
print("*** Generador de Email ***")

#Variables
nombre_usuario = "Lionel Espadas Anguas"
nombre_empresa = "Global Mentoring"
nombre_dominio = ".com.mx"

#Metodos
print(f"Nombre de usuario: {nombre_usuario}")

primer_nombre = nombre_usuario[0:7]
primer_apellido = nombre_usuario[7:14]
segundo_apellido = nombre_usuario[14:21]
usuario_normalizado = f"{primer_nombre.strip()}.{primer_apellido.strip()}.{segundo_apellido.strip()}"

nombre_empresa1 = nombre_empresa[0:6]
nombre_empresa2 = nombre_empresa[7:17]
dominio_normalizado = f"@{nombre_empresa1.strip()}{nombre_empresa2.strip()}{nombre_dominio.strip()}"

email = usuario_normalizado + dominio_normalizado

print(f"Nombre usuario normalizado: {usuario_normalizado.lower()}")
print()
print()
print(f"Nombre Empresa: {nombre_empresa}")
print(f"Extension del dominio: {nombre_dominio}")
print(f"Dominio de email normalizado: {dominio_normalizado.lower()}")
print()
print()
print(f"Email final generado: {email.lower()}")
'''
print("*** Generador de Email ***")

#variables
nombre_usuario = "Lionel Espadas Anguas"
nombre_empresa = "Global Mentoring"
dominio = ".com.mx"

nombre_normalizado = nombre_usuario.replace(" ", ".").lower()
empresa_nomralizado = nombre_empresa.replace(" ", "").lower()
dominio_nomrmalizado = f"@{empresa_nomralizado}{dominio}"
email = nombre_normalizado + dominio_nomrmalizado

print(f"Nombre usuario: {nombre_usuario}")
print(f"Nombre usuario normalizado: {nombre_normalizado}")
print(f"\nNombre empresa: {nombre_empresa}")
print(f"Extencion del dominio: {dominio}")
print(f"Dominio de email normalizado: {dominio_nomrmalizado}")
print(f"\nEmail final generado: {email}")
