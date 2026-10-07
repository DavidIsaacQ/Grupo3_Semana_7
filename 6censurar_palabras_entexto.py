
texto = "Este texto contiene una palabra mala y otra prohibida."
prohibidas = ["mala", "prohibida"]

for palabra in prohibidas:
    texto = texto.replace(palabra, "*" * len(palabra))

print(texto)