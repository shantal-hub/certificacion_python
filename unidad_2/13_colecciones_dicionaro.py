persona={
    "nombre":"isabel",
    "edad":16,
    "profesion":"ingenieria",
    "estudiante":"False"
}
print(persona)
print(persona["estudiante"])
print(persona["nombre"])
print(persona.get("edad"))

persona["edad"]=67
print(persona.get("edad"))
#Agregar un par(clave:valor)
persona["ciudad"]="san pepe racho"
print(persona)
#RECORRER DICIONARIO CON UN BLUCLE
for clave,valor in persona.items():
    print(f"{clave}:{valor}")