#Ejercicio 4: realizar un programa que filtre si eres apto para registrar un negocio
##condiciones: mayor de edad, tener ruc y tener un nombre comercial 
print("Registro de negocio")
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
edad = int(input("ingrese su edad: "))
if edad>=18: 
    print("a partir de la siguiente pregunta binaria, responda escribiendo 0 en caso la respuesta sea negativa (no) \ny 1 en caso la respuesta sea positiva (si)")
    ruc = int(input("indicar si cuenta o no con RUC: "))
    comercial = int(input("indicar si cuenta o no con un nombre comercial: "))
    if ruc==1 and comercial==1: 
        num_ruc = input("indicar su numero de ruc: ")
        nombre_comercial = input("indicar el nombre comercial de su negocio: ")
        msg0 = f"Hola {nombre}, usted califica como APTO para registrar un negocio. \nSe procederá a registrarlo como {nombre_comercial} con N° de RUC {num_ruc}"
        print(msg0)
    else: 
        msg1 = f"Hola {nombre}, usted califica como NO APTO para resgistrar un negocio"
        print(msg1)
       
else: 
    msgError = f"Hola {nombre}, usted califica como NO APTO para resgistrar un negocio por ser menor de edad"
    print(msgError)
