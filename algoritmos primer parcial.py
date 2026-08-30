def algoritmo_bresenham():
    print("Ejecutando el algoritmo de bresemham")

    #se pudi al usuario ingresar el valor de x0,y0 y x1,y1
    x0= int(input("Ingrese el valor de x0"))
    y0= int(input("Ingrese el valor de y0"))
    x1= int(input("Ingrese el valor de x1"))
    y1= int(input("Ingrese el valor de y1"))
    #calculo de diferenciales
    dx=abs(x1-x0)
    dy=abs(y1-y0)

    #variables para guarda el nuevo punto
    x=x0
    y=x0
    #calculo de pk
    pk = 2*dy - dx
    while x1 != x and y1 != y :
        if dx > dy:#en caso de que dx sea mayor a dy

            if pk < 0:
                if x0 < x1:
                    x = x+1
                else :
                    x = x-1
            elif pk >= 0:
                if x0 < x1:
                    x = x+1
                else :
                    x = x-1
                if y0 < y1: 
                    y = y+1
                else :
                    y = y-1

        #en caso de que dx sea menor o igual a dy
        elif dx <= dy:
            pk = 2*dx - dy 
 

    




while True:
    print("Elije el agoritmo que deseas usar")
    print("Presiona el numero 1 para algoritmo de bresenham")
    opcion = input()
    #menu de seleccion para el algoritmo
    match opcion:
        case "1":

            algoritmo_bresenham()


