"""
Programa: Cálculo del área de un rectángulo
Autor: MAYRA MORAN MEDINA
Carrera: TEGNOLOGIAS DE LA INFORMACION
Nivel: SEGUNDO SEMESTRE
Correo: MM.MORANM@UEA.EDU.EC

Descripción:
Este programa calcula el área de un rectángulo a partir del ancho y
alto ingresados por el usuario. Demuestra el uso de tipos de datos,
identificadores y buenas prácticas en Python.
"""

def calcular_area_rectangulo(ancho, alto):
    area = ancho * alto
    return area


def main():
    nombre_usuario = input("Ingrese su nombre: ")
    ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
    alto_rectangulo = float(input("Ingrese el alto del rectángulo: "))

    area_resultado = calcular_area_rectangulo(ancho_rectangulo, alto_rectangulo)
    area_valida = area_resultado > 0

    print("\n--- RESULTADOS ---")
    print(f"Usuario: {nombre_usuario}")
    print(f"Área del rectángulo: {area_resultado:.2f}")

    if area_valida:
        print("El área calculada es válida.")
    else:
        print("El área calculada no es válida.")


if __name__ == "__main__":
    main()
