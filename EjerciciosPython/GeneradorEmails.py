# Generador de emails

print('***  Generador de Emails  ***')

#Nombre completo del usuario
nombre_completo = ' Maria Martinez Martinez '
print((f'Nombre usuario: {nombre_completo}'))

#Normalizar el nombre del usuario
#Limpiamos los espacios en blanco al inicio y al final
nombre_normalizado = nombre_completo.strip()

#Reemplazar los espacios en blanco por puntos
nombre_normalizado= nombre_normalizado.replace(' ', '.')

#Convertimos todo a minusculas
nombre_normalizado = nombre_normalizado.lower()
print(f'Nombre de usuario normalizado: {nombre_normalizado}')

# Datos de la Empresa
nombre_empresa = ' Global Mentoring '
print(f'\nNombre empresa : {nombre_empresa}')
extension_dominio = '.com.es'
print(f'Extensión del dominio : {extension_dominio}')

#Quitar los espacios en blanco y convertimos a mayúsculas
nombre_empresa_normalizado = nombre_empresa.replace(' ','').lower()
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{extension_dominio}'
print(f'Dominio del email normalizado: {dominio_email_normalizado}')

#Creamos el email final
email = f'{nombre_normalizado}{dominio_email_normalizado}'
print(f'\nEmail final generado: {email}')
