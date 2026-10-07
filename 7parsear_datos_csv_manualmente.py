
datos = ["Ana,18,Lima", "Luis,15,Cusco", "Carlos,20,Arequipa"]

for linea in datos:
    nombre, nota, ciudad = linea.split(",")
    print(f"Nombre: {nombre} | Nota: {nota} | Ciudad: {ciudad}")