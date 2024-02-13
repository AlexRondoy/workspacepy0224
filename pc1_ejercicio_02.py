#Ejercicio 2: realizar un programa que calcule el area y el perimetro de un poligono a tu elección 
import math 
print("Calculamos el perimetro y area de un cuadrado")
lado = int(input("ingrese la medida (en metros) de uno del lado del cuadrado: "))
perimetro = lado*4
area = math.pow(lado,2)
msg = f"El cuadrado tiene un perimetro de {perimetro} metros y el area es de {area} m2"
print(msg)