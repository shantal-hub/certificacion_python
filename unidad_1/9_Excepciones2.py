try:
    #Ejemplo 1 sin manejo de exsepciones
    numero1=int(input("Ingresa el primer numero:"))
    numero2=int(input("Ingresa el primer numero:"))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("DIVISION ENTRE CERO FALLIDA")
except ValueError:
    print("Te pidieron numeros choyo")
else:
    print("el resultado", resultado)
finally:
    print("programa finalizado")