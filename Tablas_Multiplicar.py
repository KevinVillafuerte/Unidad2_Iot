#Tablas_Multiplicar
class TablasMu():
    def imprimir_tabla(numero):
        limite = 10
        contador = 1
        while contador <= limite:
            resultado = contador * numero
            print("{} x {} = {}".format(numero, contador, resultado))
            contador = contador + 1

    print("Tabla 1")
    imprimir_tabla(1)
    print("       ")
    print("Tabla 2")
    imprimir_tabla(2)
    print("       ")
    print("Tabla 3")
    imprimir_tabla(3)
    print("       ")
    print("Tabla 4")
    imprimir_tabla(4)
    print("       ")
    print("Tabla 5")
    imprimir_tabla(5)
    print("       ")
    print("Tabla 6")
    imprimir_tabla(6)
    print("       ")
    print("Tabla 7")
    imprimir_tabla(7)
    print("       ")
    print("Tabla 8")
    imprimir_tabla(8)
    print("       ")
    print("Tabla 9")
    imprimir_tabla(9)
    print("       ")
    print("Tabla 10")
    imprimir_tabla(10)
