print("ingresa tu nombre y apellido")
nombre = input()
#Opcion 1
print ("Bienvenido:")
print (nombre)
#Opcion 2
print ("bienvenido:", nombre)
#Calcular el IMC de esa persona
#Leer peso, altura
peso = input("Ingresa tu peso en kilogramos:")
peso = float(peso)
altura = input("Ingresa tu talla en metros:")
altura = float(altura)
#Calculos
imc = peso/altura**2
#mostrar imc
print("tu IMC = ", imc)
#clasificacion segun el IMC
if 18.5<=imc<=24.9:
    print("clasificacion normal")
else:
    if 25<=imc<=29.9:
        print("clasificacion sobre peso")
    else:
        if 30<=imc<=34.9:
            print("clasificacion obesidad 1")
        else: 
            if 35<=imc<=39.9:
                print("Clasificacion obesidad 2")
            else:
                if imc>=40:
                    print("clasificacion obesidad extrema")
                   

