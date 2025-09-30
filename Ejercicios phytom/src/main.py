#Función principal
'''
numero = int(input("Ingrese un número entero mayor que 1: "))
mod_funciones.primo(numero)
variable = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
mod_funciones.fibonacci(variable)
multiplicando = int(input("Ingrese el número entero: "))
mod_funciones.tabla(multiplicando)
'''

from modulo_funciones import *

def main():
    while True:
        opc = menu()
        match opc:
            case 1:
                print("calcula si un numero es primo")
                valor = int(input("Ingresa un entero mayor que 1 >>"))
                primo(valor)
            case 2:
                print("imprime la serie de fibonacci.")
                num = int(input("Ingresa el numero de terminos >>"))
                fibonacci(num)
            case 3:
                print("imprime la tabla de multiplicar")
                num = int(input("Ingresa el numero >>"))
                tabla(num)
            case 4:
                break
            case _:
                print("opcion no valida")


if __name__ == "__main__":
    main()

