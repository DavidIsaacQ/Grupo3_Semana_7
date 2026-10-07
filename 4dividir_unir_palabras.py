
cadena = "rojo,verde,azul,amarillo"
colores = cadena.split(",")
resultado = " | ".join(color.upper() for color in colores)
print(resultado)