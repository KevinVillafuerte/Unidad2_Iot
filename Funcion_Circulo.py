#Funcion_para_calcular_Perimetro_de_un_Circulo
from math import pi
class ciculo():
        def circle_perimeter(radio):
                radio = float(radio)
                perimeter = 2 * pi * radio
                return format(perimeter, ".1f")
        def cicle_area(radio):
                radio = float(radio)
                area = pi * radio ** 2
 
                return format(area, ".1f")
        #Perimetro
        radio = input("Ingrese el radio del circulo : ")
        result_per = circle_perimeter(radio)
         
        #Area
        result_ar = cicle_area(radio)
         
        print("Perimetro:", result_per + " cm")
        print("Area:", result_ar + " cm2")
