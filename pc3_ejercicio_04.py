#Ejercicio 04
#crear un archivo nuevo y realizar una funcion que permita dividir 2 numeros, importar esta funcion
# ponerlo en un bucle while True , y al ser llamada la importacion ponerlo dentro de un try except 
# ejecutar la funcion hasta que realice correctamente la division luego de eso romper el bucle

from base.file import dividir
while True:
    try:
        m=float(input("ingrese el dividendo:"))
        n=float(input("ingrese el divisor:"))
        resultado=dividir(m,n)
        print(resultado)
    except Exception as error:
        print(error)

