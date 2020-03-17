#Area Circulo
from math import pi
from tkinter import *
from tkinter import messagebox

def operar():
    areaAux=rad.get()
    areaRes=pi*pow(areaAux,2)
    messagebox.showinfo(title="Ejercicio Circulo", message="El area es: " + str(areaRes))

window = Tk()
window.title("Area del Circulo")
window.geometry("500x300+100+100")
lblTitulo=Label(text='Cual es la longitud y el area del circulo ?',font=("Areal",14)).pack()

lblRadio=Label(text="Ingrese el radio del circulo: ",font=("Areal",10)).place(x=10, y=40)
rad=IntVar()
txtRadio=Entry(window,textvariable=rad).place(x=190,y=48)

btnResultado=Button(window,text="Calcular Area",command=operar,font=("Areal",10)).place(x=190, y=110)
 

