
def validar_email(email):
    email = email.strip().lower()

    if "@" in email and "." in email:
        dominio = email.split("@")[1]
        return dominio
    else:
        return "Email inválido"

email = input("Ingresa tu email: ")
print(validar_email(email))