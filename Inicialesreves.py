#Iniciales_reves.py
from tkinter import *
from tkinter import messagebox

class CadenaReves():
        def __init__(self):
                self.window = Tk()
                self.window.title("Palabra Reves")
                self.window.geometry("300x200")

                self.lbl_n1 = Label(self.window, text="Palabra:")
                self.lbl_n1.pack()
                n1 = DoubleVar()
                self.txt_n1 = Entry(self.window, textvariable=n1)
                self.txt_n1.pack()

                self.btn_leer = Button(self.window, text = "Leer Cadena", command=self.cadena)
                self.btn_leer.pack()
        def cadena(self):
                palabra = input("ingrese palabra: ")
                n = 0
                alreves = " "
                k = len(palabra)-1
                while(n <= k):
                    alreves = alreves + palabra[k]
                    k = k-1
                messagebox.showinfo(message="palabra alreves es:")

calc = CadenaReves()

