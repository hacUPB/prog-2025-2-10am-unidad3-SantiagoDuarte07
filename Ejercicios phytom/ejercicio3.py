# Ejercicio simple
### Se le pide al usuario que ingrese un numero entero y que muestre un mensaje si el numero es divisible por 3.

numero = int(input("Ingrese un numero entero: "))
residuo = numero%3
if residuo == 0:
    print(numero, "divisible entre 3")
else:
    print(numero, "no divisible entre 3")
    