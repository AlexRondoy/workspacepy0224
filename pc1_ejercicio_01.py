#Ejercicio 1: realizar un programa que pida tus datos personales y mostrar en pantalla los datos solicitados 
nombre = input("ingrese su nombre completo: ")
apellidos = input("ingrese sus apellidos: ")
edad = input("ingrese su edad: ")
dni = input("ingrese el numero de su documento de identidad: ")
direccion = input("ingrese su dirección: ")
telefono = input("ingrese su numero de telefono: ")
msg = f"{nombre} {apellidos} \n{edad} \n{dni} \n{direccion} \n{telefono} "
print(msg) 