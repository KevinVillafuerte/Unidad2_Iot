#Conversion del Dolar
from tkinter import *
from tkinter import messagebox

interfaz = Tk()

def convertir():
    dPesos= dolares.get()*pDolar.get()
    messagebox.showinfo(title= "Ejercicio Dolares", message= str(dolares.get())+"Dolares equivalen a :"+str(dPesos)+"Pesos $")

interfaz.geometry("500x300+100+100")
lblTitle = Label(text="Conversion de Dolar", font=("Arial", 14)).pack()

lblDolar = Label(text="Ingrese el precio actual del Dolar: ", font=("Arial", 12)).place(x=10, y=40)
pDolar = DoubleVar()
txtIngrese=Entry(interfaz, textvariable = pDolar).place(x=270, y=48)

lblDolares = Label(text="Ingrese la cantidad de Dolares a convertir: ", font=("Arial", 12)).place(x=10, y=70)
dolares = DoubleVar()
txtIngrese=Entry(interfaz, textvariable = dolares).place(x=320, y=78)

btnResutado = Button(interfaz, text="Convertir", command=convertir, font=("Arial", 12)).place(x=10, y=110)

interfaz.mainloop()
