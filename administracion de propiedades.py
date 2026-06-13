piso1 = {
    "101": "juan velez",
    "102": "maria soto"
    }
piso2 = {
    "201": "pedro rojas",   
    "202": "ana diaz"
    }
piso3 = {
    "301": "carlos perez",
    "302": "claudia torres"
    }
piso4 = {
    "401": "jose gonzales",
    "402": "camila muñoz"
    }



print("dueño del departamento 202: ",piso2["202"])
print("-"*30)

piso3["302"] = "juan velez"
print("piso3 actualizado:")
for clave, valor in piso3.items():
    print(clave, valor)
    
print("-"*30)
piso1 ["103"] = "pedro sanchez"
print("piso1 actualizado:")
for clave, valor in piso1.items():
    print(clave,valor)
print("-"*30)

del piso4["402"]
print("piso4 actualizado:")

for clave, valor in piso4.items():
    print(clave,valor)
print("-"*30)

print("departamentos piso2:")
for clave, valor in piso2.items():
    print(clave,valor)
print("-"*30)

print("cantidad de departamentos en el piso1: 3")

print("-"*30)

print("propietarios piso3")
for valor in piso3.values():
    print(valor)



