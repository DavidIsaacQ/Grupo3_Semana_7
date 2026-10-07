# #Enunciado6 –CENSURAR PALABRA EN UN TEXTO:
# Dada una lista de palabras prohibidas, reemplaza cada aparición 
# en un texto por asteriscos del mismo largo.

texto = "Hola negro como estas hdp"

palabras_prohibidas = ["negro", "hdp"]

for palabra in palabras_prohibidas:
    if palabra in texto:
        texto = texto.replace(palabra,'*'*len(palabra))

print (texto)
