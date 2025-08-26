print("=== MENÚ PRINCIPAL ===")
print("1. Ver datos de sensores")
print("2. Configurar parámetros")
print("3. Salir")

opcion = int(input("Selecciona una opción: "))

match opcion:
    case "A":
        print("Mostrando datos de sensores...")
    case "B":
        print("Entrando a configuración...")
    case "C":
        print("Saliendo del programa...")
    case "D":
        print("Opción inválida.")