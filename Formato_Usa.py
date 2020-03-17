#Formato_Usa
from tkinter import *
from tkinter import messagebox

class Usa:
    def __init__(self):
        self.window = Tk()
        self.window.title("Formato Usa")
        self.window.geometry("200x150")

        self.lbl_n1 = Label(self.window, text="Solo formato con decimales")
        self.lbl_n1.pack()
        self.lbl_n1 = Label(self.window, text="Calificacion")
        self.lbl_n1.pack()
        n1 = DoubleVar()
        self.txt_n1 = Entry(self.window,textvariable=n1)
        self.txt_n1.pack()

        self.btn_accion = Button(self.window, text="Operar", command=self.operar)
        self.btn_accion.pack()

    def operar(self):
        self.k = ""
        self.m = float(self.txt_n1.get())
        if self.m >= 9.0 and self.m <= 10.0:
            self.k = "A"
        elif self.m >= 8.0 and self.m <= 8.9:
            self.k = "B"
        elif self.m >= 7.5 and self.m <= 7.9:
            self.k = "D"
        elif self.m <= 7.4:
            self.k = "F"
        messagebox.showinfo(message=self.k, title="Resultado")

calc = Usa()   

        
