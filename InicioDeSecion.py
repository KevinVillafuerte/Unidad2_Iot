# InicioSesion.py
from tkinter import *
from tkinter import messagebox

class LoginGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Inicio de Sesion")
        self.window.geometry("300x200")

        self.lbl_n1 = Label(self.window, text="Usuario:")
        self.lbl_n1.pack()
        n1 = DoubleVar()
        self.txt_n1 = Entry(self.window, textvariable=n1)
        self.txt_n1.pack()
        
        self.lbl_n2 = Label(self.window, text="Contraseña:")
        self.lbl_n2.pack()
        n2 = DoubleVar()
        self.txt_n2 = Entry(self.window, textvariable=n2)
        self.txt_n2.pack()

        self.btn_iniciar = Button(self.window, text = "Iniciar Sesion", command=self.Sesion)
        self.btn_iniciar.pack()

    def Sesion(self):
            if self.txt_n1.get() == "utng" and self.txt_n2.get() == "mexico":
                messagebox.showinfo(message="Bienvenido", title="Hola Mundo")

calc = LoginGUI()
