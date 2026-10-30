#creando una tupla 
coordenadas=(10.5,20.3,30.3)
nombres=("pablo","isa","mayte")
for indice,coordenadas in enumerate(coordenadas):
    print(f"[{indice}]coordenadas[{coordenadas}]")
coordenadas[0]=30.9
print(coordenadas[0])