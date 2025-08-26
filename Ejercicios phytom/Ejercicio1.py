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
if imc<18.5:
    mensaje = "bajo peso"
elif imc<25:
    mensaje = "peso normal"
elif imc<30:
    mensaje = "sobre peso"
elif imc<35:
    mensaje = "obesidad tipo 1"
elif imc<40:
    mensaje = "obesidad tipo 2"
else:
    mensaje = "obesidad extrema"

print(f"Paciente {nombre}, tiene un IMC de {imc:0.2f} y su condicion de {mensaje}")