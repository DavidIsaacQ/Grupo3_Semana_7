# #Enunciado9 –ANALIZAR FRECUENCIA DE PALABRAS:
# Escribe una función que reciba un párrafo de texto y retorne 
# un diccionario con la frecuencia de cada palabra, 
# ignorando signos de puntuación, mayúsculas y 
# palabras vacías (stopwords)

def analizar_frecuencia(parrafo):

    texto_limpio = parrafo.lower().replace(".", "")
    
    stopwords = ["es", "un", "de", "la", "y", "en"]
    
    frecuencias = {}
  
    for palabra in texto_limpio.split():
        if palabra not in stopwords:
            if palabra in frecuencias:
                frecuencias[palabra] = frecuencias[palabra] + 1
            else:
                frecuencias[palabra] = 1
                
    return frecuencias

texto_prueba = "Python es un lenguaje. Aprender Python es divertido"
resultado = analizar_frecuencia(texto_prueba)
print(resultado)
