# importacion de librerias
import matplotlib.pyplot as plt


def graficar_puntos(puntos, x0, y0, x1, y1):
    """Recibe la lista de tuplas [(x, y), ...] y genera el gráfico."""
    if not puntos:
        print("No hay puntos para graficar.")
        return

    # hacemos una lista de las coordenadas en "x" y de "y"
    xs = [p[0] for p in puntos]
    ys = [p[1] for p in puntos]

    plt.figure("Trazado con Algoritmo de Bresenham", figsize=(8, 6))

    # 1. Graficar los puntos obtenidos
    plt.scatter(xs, ys, color="blue", s=50, label="Píxeles (Bresenham)", zorder=3)

    # 2. Graficar la linea continua del punto inicial al final
    plt.plot(
        [x0, x1],
        [y0, y1],
        color="red",
        linestyle="--",
        alpha=0.6,
        label="Recta continua ideal",
        zorder=2,
    )

    # 3. graficacion de punto inicial y final
    plt.scatter(
        [x0], [y0], color="green", s=100, label=f"Inicio ({x0}, {y0})", zorder=4
    )
    plt.scatter([x1], [y1], color="purple", s=100, label=f"Fin ({x1}, {y1})", zorder=4)

    # configuramos limites con margen
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    margen = 2

    plt.xlim(min_x - margen, max_x + margen)
    plt.ylim(min_y - margen, max_y + margen)
    # Configuración de cuadricula
    plt.legend(bbox_to_anchor=(-0.01, 0), loc="lower right", borderaxespad=0.0)  # leyenda
    plt.title(f"Línea de Bresenham de ({x0}, {y0}) a ({x1}, {y1})")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.grid(True, which="both", linestyle=":", linewidth=0.7)

    # tamaño de cuadricula iguales
    plt.gca().set_aspect("equal", adjustable="box")

    # Muestra la ventana gráfica
    plt.show()


def algoritmo_bresenham():
    print("Ejecutando el algoritmo de bresemham")

    # se pudi al usuario ingresar el valor de x0,y0 y x1,y1
    x0 = int(input("Ingrese el valor de x0: "))
    y0 = int(input("Ingrese el valor de y0: "))
    x1 = int(input("Ingrese el valor de x1: "))
    y1 = int(input("Ingrese el valor de y1: "))

    # calculo de diferenciales
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    # variables para guarda el nuevo punto
    x = x0
    y = y0

    # calcular si avanzmos o retrocedemos
    if x0 < x1:
        paso_x = 1
    elif x0 > x1:
        paso_x = -1
    else:
        paso_x = 0

    if y0 < y1:
        paso_y = 1
    elif y0 > y1:
        paso_y = -1
    else:
        paso_y = 0

    # se usa una lista de tuplas para guardar las puntos
    puntos = []
    puntos.append((x, y))

    # calculo de pk
    if dx > dy:  # en caso de que dx > dy
        pk = 2 * dy - dx
        while x != x1 or y != y1:
            x = x + paso_x  # en este caso siempre se actualiza x
            if pk < 0:
                pk = pk + 2 * dy
            else:
                y = y + paso_y
                pk = pk + 2 * dy - 2 * dx
            puntos.append((x, y))  # guardamos el punto
    else:
        pk = 2 * dx - dy
        while y != y1:
            y = y + paso_y  # en este caso siempre se actualiza y
            if pk < 0:
                pk = pk + 2 * dx
            else:
                x = x + paso_x
                pk = pk + 2 * dx - 2 * dy

            puntos.append((x, y))  # Guardamos el nuevo punto generad

    print("\nPuntos generados por el algoritmo:")
    print(puntos)

    graficar_puntos(puntos, x0, y0, x1, y1)


def main():
    while True:
        print("===================================================")
        print("ALGORITMOS DE GRAFICACIÓN COMPUTACIONAL")
        print("===================================================")
        print("1. Algoritmo de bresenham (trazo de lineas)")
        print("0. Salir")
        opcion = input()
        # menu de seleccion para el algoritmo
        match opcion:
            case "1":

                algoritmo_bresenham()
            case "0":
                print("Saliendo del programa")
                break
            case _:
                print("Opcion no valida intente de nuevo")


if __name__ == "__main__":
    main()
