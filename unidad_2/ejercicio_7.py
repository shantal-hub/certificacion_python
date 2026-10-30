#El mapa del tesoro
mapa=[
    [".",".",".","B"],
    [".",".",".","."],
    [".","A",".","x"],
    [".",".",".","."]
]
filas=len(mapa)
columnos=len(mapa[0])

for i in range(filas):
    for j in range(columnos):
        if mapa[i][j]=="A":
            print(f"tesoro encontrado en la posicion [{i}][{j}]")
        if mapa[i][j]=="B":
            print(f"tesoro encontrado en la posicion [{i}][{j}]")