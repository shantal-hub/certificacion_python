colores=["azul","morado","rojo","amarrilo","rosa"]
color=input("Ingresa el color:")#verde
encontrado=False
for contador in colores:
    print(contador)
    #si el contador actual es "rojo", deten el bucle
    if contador==color:
        print("color encontrado! saliendo del bucle")
        encontrado=True
        break
if not encontrado:
    print("El color,",color,"no se encuentra")
