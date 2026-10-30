#cadenas y concetenacion con (+)
cadena1='hola'
cadena2="mundo"
multilinea=""" esto es una cadena
con varias lineas"""
print(cadena1 + cadena2 + multilinea)
eco="ji"*10
print(eco)
tu_nombre='Isa'
print(tu_nombre.upper())
print(tu_nombre.lower())
frase="me gusta programacion"
print(frase.replace("programacion","matematicas"))
edad=16
nombre='Isa'
mensaje=f"hola,me llamo {nombre} y tengo\n{edad}años"
print(mensaje)
texto= "¡Felicidades por aun continuar en el cecytem!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
oracion="Aprender programacion es divertido"
if "java" in oracion:
    print("encontrado")
else:
    print("no esta ")
ncadena=""
print(ncadena.isalpha())
print(ncadena.isdigit())