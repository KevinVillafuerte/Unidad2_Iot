#Calculadora_gui
from tkinter import*
from tkinter import messagebox
from calcu import Calculadora

class CalculadoraGUI:
    def __init__(self):
        window = Tk()
        self.calc = Calculadora()
        self.number1_label = Label(window, text="Numero 1:")
        self.n1 = DoubleVar()
        self.number1_entry = Entry(window, textvariable = self.n1)
        
        self.number2_label = Label(window, text="Numero 2:")
        self.n2 = DoubleVar()
        self.number2_entry = Entry(window, textvariable = self.n2)

        self.add_button = Button(window, text="Sumar",command = self.sumar)
        self.sustract_button = Button(window, text="Resta",command = self.restar)
        self.multi_button = Button(window, text="Multiplicar",command = self.multiplicar)
        self.div_button = Button(window, text="Dividir",command = self.dividir)
        self.pont_button = Button(window, text="´Potencia",command = self.potencia)
        
        self.number1_label.grid(column = 2, row= 2)
        self.number1_entry.grid(column = 4, row= 2)
        self.number2_label.grid(column = 2, row= 4)
        self.number2_entry.grid(column = 4, row= 4)
        self.add_button.grid(column =3, row= 5)
        self.sustract_button.grid(column =3, row= 6)
        self.multi_button.grid(column =4, row= 5)
        self.div_button.grid(column =4, row= 6)
        self.pont_button.grid(column =3, row= 7)

    def sumar(self):
        self.calc.suma(self.n1.get(),self.n2.get())
        messagebox.showinfo("Resultado", self.calc.result)
    def restar(self):
        self.calc.resta(self.n1.get(),self.n2.get())
        messagebox.showinfo("Resultado", self.calc.result)
    def multiplicar(self):
        self.calc.multiplicacion(self.n1.get(),self.n2.get())
        messagebox.showinfo("Resultado", self.calc.result)
    def dividir(self):
        self.calc.division(self.n1.get(),self.n2.get())
        messagebox.showinfo("Resultado", self.calc.result)
    def potencia(self):
        self.calc.potenciacion(self.n1.get(),self.n2.get())
        messagebox.showinfo("Resultado", self.calc.result)

calcu = CalculadoraGUI()
