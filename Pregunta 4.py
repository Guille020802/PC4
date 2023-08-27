# Pregunta 4

def guardar_tabla_multiplicar(numero):
    with open(f"tabla-{numero}.txt", "w") as archivo:
        for i in range(1, 11):
            linea = f"{numero} x {i} = {numero * i}\n"
            archivo.write(linea)

def mostrar_tabla(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def mostrar_linea_tabla(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if 1 <= linea <= len(lineas):
                print(lineas[linea - 1].strip())
            else:
                print("Línea no válida.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def main():
    while True:
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                guardar_tabla_multiplicar(numero)
                print(f"Tabla de multiplicar del {numero} guardada.")
            else:
                print("Número fuera de rango.")
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                mostrar_tabla(numero)
            else:
                print("Número fuera de rango.")
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea a mostrar: "))
            if 1 <= numero <= 10 and 1 <= linea <= 10:
                mostrar_linea_tabla(numero, linea)
            else:
                print("Número o línea fuera de rango.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()