import random
refrigerios = []
for _ in range (1000000):
    tipo=random.randint(1,3)
    nombre=random.choice(['Yogur', 'Barras de queso', 'Galletas saladas integrales'])
    precio=random.randint(15000, 40000)
    refrigerio = [tipo, nombre, precio]
    refrigerios.append(refrigerio)

print(refrigerios)