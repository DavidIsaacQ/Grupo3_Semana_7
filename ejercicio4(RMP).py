# #Enunciado4 –DIVIDIR Y UNIR PALABRAS:
# Dada la cadena 'rojo,verde,azul,amarillo', 
# separa los colores, ponlos en mayúsculas y únelos con ' | ' 
# como separador.

cadena = 'rojo,verde,azul,amarillo'

cadenaMAYUS = cadena.upper()

print (cadenaMAYUS.replace(",", "|"))