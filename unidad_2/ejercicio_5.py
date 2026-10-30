carrito=[]
cantidad=int(input("¿cuantos productos quieres agregar?"))
for contador in range(cantidad):
    productos=input(f"Ingresa el producto")
    carrito.append(productos)
print("\n Tu lista de compra es:")
print(carrito)