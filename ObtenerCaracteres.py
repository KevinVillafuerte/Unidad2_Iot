#Obtener Caracteres de una cadena
from tkinter import *
from tkinter import messagebox

def print_result():
    numAux=num.get()
    message=numAux[0] + "\n" + numAux[1]+ "\n" + numAux[2]+ "\n" + numAux[3]
    lblPrint = Label(text=message).place(x=210,y=10)

interfaz = Tk()
interfaz.geometry("250x110+860+470")
interfaz.title("Obtener Caracteres de Una Cadena")

lblNum= Label(text="Ingrese un numero de 4 digitos: ").place(x=10, y=10)
num=StringVar()
txtNum=Entry(interfaz, textvariable=num).place(x=40,y=40)
btnPrint=Button(interfaz, text="Imprimir", command=print_result).place(x=70,y=70)
