numero = 100
while numero >= 0:
    print(numero)
    numero -= 5       #numero = numero - 5

numero1 = int(input("ingrese el primer numero"))
numero2 = int(input("ingrese el segundo numero"))
residuo1 = numero1 %2
if numero1 < numero2:
    mayor = numero2
    menor = numero1
else:
    mayor = numero1
    menor = numero2
'''
while menor <= mayor:
    if menor % 2 == 0:
        print (menor)
    num1 += 1
'''
if menor % 2 == 1:
    menor += 1
while menor <= mayor:
    print(menor)
    menor +=2
