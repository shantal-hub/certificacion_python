carrito=[]
n_producto=int(input("Ingresa el numero de producto:"))
for i in range(n_producto):
    producto=input("Ingresa el producto al carrito:")
    carrito.append(producto)
print("lista creada correctamente")
carrito[0]="papas"
print(f"tu carrito contiene{carrito}")