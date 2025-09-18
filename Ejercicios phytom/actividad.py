num = int(input("Ingrese un numero entero para generar tabla de multiplicar"))
contador = 1
print("tabla de multiplicar del numero", num)
while contador < 11:
    res = num * contador
    print(f"{num} x {contador} = {res}")
    contador += 1
