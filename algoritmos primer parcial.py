# importacion de librerias
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def graficar_puntos(puntos, x0, y0, x1, y1):
    if not puntos:
        print("No hay puntos para graficar.")
        return

    fig, planoCartesiano = plt.subplots(figsize=(8, 8))
    fig.canvas.manager.set_window_title("Rasterización con Bresenham")

    # 1. Dibujar cada píxel como un cuadrado de 1x1 centrado en (x, y)
    for i, (px, py) in enumerate(puntos):
        # El cuadrado va de (px - 0.5, py - 0.5) con ancho 1 y alto 1
        cuadro = patches.Rectangle(
            (px - 0.5, py - 0.5 ),
            1,
            1,
            facecolor="#1f77b4",
            edgecolor="#0f3b5a",
            linewidth=0.8,
            alpha=0.85,
            zorder=3,
        )
        planoCartesiano.add_patch(cuadro)

    # 2. Resaltar los píxeles de inicio y fin con bordes de color distintivo
    # Pixel inicial (borde verde grueso)
    planoCartesiano.add_patch(
        patches.Rectangle(
            (x0 - 0.5, y0 - 0.5),
            1,
            1,
            fill=False,
            edgecolor="red",
            linewidth=2.5,
            zorder=4,
            label=f"Píxel Inicio ({x0}, {y0})",
        )
    )
    # Pixel final (borde púrpura grueso)
    planoCartesiano.add_patch(
        patches.Rectangle(
            (x1 - 0.5, y1 - 0.5),
            1,
            1,
            fill=False,
            edgecolor="red",
            linewidth=2.5,
            zorder=4,
            label=f"Píxel Fin ({x1}, {y1})",
        )
    )

    # 3. Línea continua matemática de referencia
    planoCartesiano.plot(
        [x0, x1],
        [y0, y1],
        color="red",
        linestyle="--",
        linewidth=1.8,
        label="Recta ideal continua",
        zorder=5,
    )

    # 4. Límites con margen para que la rejilla no colapse
    xs = [p[0] for p in puntos]
    ys = [p[1] for p in puntos]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    margen = 2

    lim_x_inf = min_x - margen
    lim_x_sup = max_x + margen
    lim_y_inf = min_y - margen
    lim_y_sup = max_y + margen

    planoCartesiano.set_xlim(lim_x_inf, lim_x_sup)
    planoCartesiano.set_ylim(lim_y_inf, lim_y_sup)

    # 5. Configuración de la rejilla tipo "malla de píxeles"
    # Las líneas de la cuadrícula coinciden con los bordes de los píxeles (... -0.5, 0.5, 1.5, ...)
    planoCartesiano.set_xticks(np.arange(lim_x_inf, lim_x_sup + 1, 1))
    planoCartesiano.set_yticks(np.arange(lim_y_inf, lim_y_sup + 1, 1))
    planoCartesiano.set_xticks(np.arange(lim_x_inf - 0.5, lim_x_sup + 1.5, 1), minor=True)
    planoCartesiano.set_yticks(np.arange(lim_y_inf - 0.5, lim_y_sup + 1.5, 1), minor=True)

    # La cuadrícula minor marca los bordes de las celdas
    planoCartesiano.grid(which="minor", color="gray", linestyle="-", linewidth=0.5, alpha=0.5)
    planoCartesiano.grid(which="major", color="black", linestyle=":", linewidth=0.3, alpha=0.3)

    # Elemento ficticio para incluir el color azul en la leyenda
    patch_leyenda = patches.Patch(
        facecolor="#1f77b4", edgecolor="#0f3b5a", label="Píxeles activos"
    )
    handles, labels = planoCartesiano.get_legend_handles_labels()
    handles.insert(0, patch_leyenda)
    labels.insert(0, "Píxeles activos")

    planoCartesiano.legend(
        handles=handles,
        labels=labels,
        bbox_to_anchor=(1.05, 1),
        loc="upper left",
        borderaxespad=0.0,
    )

    planoCartesiano.set_title(f"Rasterización Bresenham: ({x0}, {y0}) a ({x1}, {y1})")
    planoCartesiano.set_xlabel("Coordenada X (Píxel)")
    planoCartesiano.set_ylabel("Coordenada Y (Píxel)")
    planoCartesiano.set_aspect("equal", adjustable="box")
    plt.tight_layout()

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
