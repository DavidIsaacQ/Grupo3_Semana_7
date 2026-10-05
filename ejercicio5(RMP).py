# #Enunciado5 –VALIDAR Y FORMATEAR CORREO ELECTRÓNICO:
# Escribe una función que reciba un email, lo limpie (strip+lower), 
# verifique que contiene '@' y '.' y retorne el dominio.

def correo (email):
    email_formateado = email.strip().lower()

    if '@' in email_formateado and '.' in email_formateado:
        dominio = email_formateado.split('@')[-1]
        return dominio
    else:
        return "Correo invalido"

usuario = correo("     ISENGARDXD@gmail.com") #Valido
usuario2 = correo("prueba_decorreo.com") #invalido

print (usuario)
print (usuario2)