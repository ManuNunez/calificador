from registro import registrar_alumno

def main():
    while True:
        print("Registro de Alumno")
        nombre = input("Nombre del alumno: ")
        grado = input("Grado: ")
        grupo = input("Grupo: ")
        aciertos = input("Aciertos: ")

        try:
            aciertos = int(aciertos)
        except ValueError:
            print("Los aciertos deben ser un número entero.")
            continue

        registrar_alumno(nombre, grado, grupo, aciertos)

        otra = input("¿Deseas registrar otro alumno? (s/n): ").lower()
        if otra != 's':
            break

if __name__ == "__main__":
    main()
