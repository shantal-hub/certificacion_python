nombre_cliente = str(input("ingresa el nombre del cliente: "))

precio1_str = str(input("precio del articulo:"))
precio2_str = str(input("precio del articulo:"))
precio3_str = str(input("precio del articulo:"))

precio1 = float(precio1_str)
precio2 = float(precio2_str)
precio3 = float(precio3_str)

total = precio1 + precio2 + precio3

print("Ticket de la compra")
print("Cliente:",nombre_cliente)
print("Total de la compra:",total)