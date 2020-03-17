# GUI_Area Trapeceo
from tkinter import *
from tkinter import messagebox

class AreaGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Area del Trapeceo")
        self.window.geometry("200x250")

        self.lbl_n1 = Label(self.window, text="Base Mayor:")
        self.lbl_n1.pack()
        n1 = DoubleVar()
        self.txt_n1 = Entry(self.window, textvariable=n1)
        self.txt_n1.pack()

        self.lbl_n2 = Label(self.window, text="Base Menor:")
        self.lbl_n2.pack()
        n2 = DoubleVar()
        self.txt_n2 = Entry(self.window, textvariable=n2)
        self.txt_n2.pack()
        
        self.lbl_n3 = Label(self.window, text="Altura:")
        self.lbl_n3.pack()
        n3 = DoubleVar()
        self.txt_n3 = Entry(self.window, textvariable=n3)
        self.txt_n3.pack()

        self.btn_sumar = Button(self.window, text = "Operar", command=self.operar)
        self.btn_sumar.pack()

    def operar(self):
            self.r = 0.0
            self.r = (float(self.txt_n1.get())+float(self.txt_n2.get())*float(self.txt_n3.get()))/2
            messagebox.showinfo(message=self.r, title="Resultado")

calc = AreaGUI()
