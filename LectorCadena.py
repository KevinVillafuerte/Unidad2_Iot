#Lector_de_Cadenas.py
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
"""
from tkinter import *
from tkinter import messagebox

class Lector:
    def __init__(self):
        self.window = Tk()
        self.window.title("Lector de Cadena")
        self.window.geometry("200x150")

        self.lbl_n1 = Label(self.window, text="Palabra:")
        self.lbl_n1.pack()
        n1 = DoubleVar()
        self.txt_n1 = Entry(self.window, textvariable=n1)
        self.txt_n1.pack()

        self.btn_accion = Button(self.window, text="Leer", command=nombrePropio(x))
        self.btn_accion.pack()

        def longitudCadena(x):
            contador = 0
            for i in x:
                contador+=1
            return contador
        def nombrePropio(x):
            y = x.lower()
            return y[0].upper()+y[1:]
            messagebox.showinfo(message = (nombrePropio(x),'tiene',longitudCadena(x),' caracteres.'))

    
calc = Lector()
        
