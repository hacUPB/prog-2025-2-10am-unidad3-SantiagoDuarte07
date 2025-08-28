control = True

while control == True:
    print("S. Sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nP. Potenciacion\nZ. Racionalizacion\nE. Salir")
    numero1 = int(input("ingrese el primer numero"))
    numero2 = int(input("ingrese el segundo numero"))
    opcion = input("Selecciona una opción: ")
    opcion = opcion.upper()
    match opcion:
        case "S":
            print("Suma")
            Resultado = numero1 + numero2
        case "R":
            print("Resta")
            Resultado = numero1 - numero2
        case "M":
            print("Multiplicacion")
            Resultado = numero1 * numero2
        case "D":
            print("Division")
            Resultado = numero1 / numero2
        case "P":
            print("Potenciacion")
            Resultado = numero1 ** numero2
        case "Z":
            print("Racionalizacion")
            Resultado = numero1 ** (1/numero2)
        case "E":
            break
        case "E":
            print("Modo no valido")
    print(f"Resultado = {Resultado}")
