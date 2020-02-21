#Lectoe_de_Cadenas.py
"""
class nombre_clase:
def nombreMetodo(Self):
def __init__
"""
def longitudCadena(x):
    contador = 0
    for i in x:
        contador+=1
    return contador
def nombrePropio(x):
    y = x.lower()
    return y[0].upper()+y[1:]
x=input('Ingrese una palabra: ')
print(nombrePropio(x),'tiene',longitudCadena(x),' caracteres.')
