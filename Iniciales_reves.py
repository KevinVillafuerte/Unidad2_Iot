#Iniciales_reves.py

class CadenaReves():
        palabra = input("ingrese palabra: " )
        n = 0
        alreves = " "
        k = len(palabra)-1
        while(n <= k):
            alreves = alreves + palabra[k]
            k = k-1
        print ( "palabra alreves es:", alreves)

