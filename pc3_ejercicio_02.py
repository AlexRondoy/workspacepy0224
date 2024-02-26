#Ejercicio 02
#Realizar un programa que tenga una clase producto el cual solo tiene los atributos de nombre y codigo
# el codigo tiene la siguiente estructura PAIS-LOTE-AÑO ejemplo:PERU-00001-2024 crear un metodo que imprima el objeto de forma 
# literal (__str__) y que permita identificar el pais de origen y nro de lote

class Producto:
    nombre:None
    codigo_producto:None
    pais:None
    lote:None
    año:None
    def __init__(self,nombre,pais,lote,año):
        self.nombre=nombre
        self.pais=pais
        self.lote=lote
        self.año=año
        self.codigo=self.generar_codigo()
    def generar_codigo(self):
        return f"{self.pais}-{self.lote}-{self.año}".upper()
    def __str__(self):
        return f"se creo el producto {self.nombre} con codigo {self.codigo}"

producto1=Producto("jabon","alemania","00052",2008)
print(producto1)
