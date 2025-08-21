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
