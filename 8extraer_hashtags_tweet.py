
def extraer_hashtags(texto):
    hashtags = [palabra.lower() for palabra in texto.split() if palabra.startswith("#")]
    return sorted(hashtags)

tweet = "Hoy aprendemos #Python y #Programacion. También usamos #Cadenas"
print(extraer_hashtags(tweet))