
def frecuencia_palabras(parrafo):
    stopwords = ["el", "la", "los", "las", "de", "y", "en", "un", "una", "es"]
    frecuencia = {}

    palabras = parrafo.lower().split()

    for palabra in palabras:
        palabra = palabra.strip(".,;:!?¿¡")

        if palabra not in stopwords:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    return frecuencia


texto = "El Python es un lenguaje. Python es fácil y Python es divertido."

print(frecuencia_palabras(texto))