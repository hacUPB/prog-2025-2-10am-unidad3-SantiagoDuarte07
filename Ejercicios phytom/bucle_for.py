
n = int(input("ingrese un numero entero"))
acum = 0
while n < 0:
    n = int(input("ingrese un numero positivo"))
acum = 0
for cont in range(0, n, 2):
    if cont %2 == 0:
        acum += cont
print(f"La suma de los pares es: {acum}")

mensaje = "Junior tu papa"
n = int(input("ingrese un numero entero positivo"))
for cont in range(0, n, 1):
    print(mensaje)
