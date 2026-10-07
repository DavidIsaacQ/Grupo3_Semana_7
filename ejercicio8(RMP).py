# #Enunciado8–EXTRAERHASHTAGSDEUNTWEET:
# Dado un texto de tweet, extrae todos los hashtags (#palabras) 
# y devuélvelos en una lista ordenada y en minúsculas


tweet = "Aprendiendo #Python con nuevos retos de #programacion y #Codigo básico!"

palabras = tweet.split()

hashtags = []
for palabra in palabras:
    if palabra.startswith("#"):
        
        hashtag_limpio = palabra.lower()
        hashtags.append(hashtag_limpio)

hashtags.sort()

print(hashtags)
