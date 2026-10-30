promedio=[7,8,10,2,9]
#1.Encontar el promedio mas bajo y el mas alto en ciclo for
#suponemos inicialmente el promedio mas bajo y mas alto como es el  primer elemento
promedio_bajo=promedio[0]
for contador in promedio:
    if contador<promedio_bajo:
        promedio_bajo=contador
print(promedio_bajo)
promedio_alto=promedio[0]
for contador in promedio:
    if contador>promedio_alto:
        promedio_alto=contador
print(promedio_alto)








