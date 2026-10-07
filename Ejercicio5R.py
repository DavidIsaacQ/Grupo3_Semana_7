# Ejercicio 5 - Validar y formatear correo electronico

email = input("Ingrese su e-mail: ")

email_limpio = email.strip().lower()
partes = email_limpio.split("@")

print(f"El dominio es {partes[1]}")
