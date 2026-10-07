# #Enunciado7 –PARSEAR DATOS CSV MANUALMENTE:
# Dadas varias líneas CSV con formato 'nombre,nota,ciudad',
#  extrae la información y muestra un reporte formateado

lineas_csv = ["Rodolfo Muñante,15,LIMA", "Aquiles esquivel,11.5,SJL", "Tutan Camon,18,HUAROCONDO"]
print ("REPORTE DE NOTAS")

for linea in lineas_csv:
    print(linea.split(","))
