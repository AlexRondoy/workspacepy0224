base_datos=[]
promedio_final=[]
promedios_finales=[]
alumnos_aprobados=[]
alumnos_desaprobados=[]
def datos_personales():
    name=input("ingrese su nombre: ")
    msg=f"Hola {name},registre los siguientes datos personales"
    print(msg)
    surname=input("ingrese su primer apellido: ")
    age=input("ingrese su edad: ")
    correo=input("ingrese su correo: ")
    matematica=int(input("ingrese su nota de matematica: "))
    comunicacion =int(input("ingrese su nota de comunicación: "))
    datos={"nombre":name,"edad":age,"correo":correo,"cursos":[{"nombre de curso ":["matematica","comunicación"],"notas":[matematica,comunicacion]}]}
    base_datos.append(datos)
def operacion_matematica():
    number_1=int(input("ingrese un numero: "))
    number_2=int(input("ingrese otro número"))
    return number_1+number_2
def funcion_rango(n1:int,n2:int):
    multiplos=[]
    lista_mayor=[*range(n1,n2,1)]
    for i in lista_mayor:
        if i%2==0:
            multiplos.append(i)
        elif i%5==0:
            multiplos.append(i)
        elif i%7==0:
            multiplos.append(i)
        else:
            continue
    print("lista de numeros multiplos de 2,5 y 7",multiplos)
    print("tamaño de la lista multiplo,",len(multiplos))
def numero_mayor(a:int,b:int):
    if a>b:
        return a
    else:
        return b 
print("Bienvenido al menú iterativo")
while True:
    print("""""""""¿Que quieres hacer? Escribe una opción
    1) ingresar datos personales
    2) sumar dos números
    3) verificar datos y notas 
    4) ver lista de promedios finales 
    5) ver alumnos aprobados
    6) ver alumnos desaprobados
    7) ingresar rango de numeros y ver lista de numeros multiplos(2,5 y 7)
    8) ingresar dos numeros y ver el numero mayor
    9) salir""""""""")
    opcion=input()
    if opcion=="1":
        datos_personales()
    elif opcion=="2":
        suma = operacion_matematica()
        print("la suma de los numeros ingresados es,",suma)
    elif opcion=="3":
         for i, item in enumerate(base_datos):
             print(i,item)
    elif opcion =="4":
        for i in base_datos:
            nota_matematica=i["cursos"][0]["notas"][0]
            nota_comunicacion=i["cursos"][0]["notas"][1]
            promedio=(nota_matematica+nota_comunicacion)/2
            promedios_finales.append(promedio)
            index=promedios_finales.index(promedio)
            if promedio>=10.5:
                alumnos_aprobados.append(base_datos[index]["nombre"])
            else: 
                alumnos_desaprobados.append(base_datos[index]["nombre"])
        print(promedios_finales)
    elif opcion=="5":
        print(alumnos_aprobados)
    elif opcion=="6":
        print(alumnos_desaprobados)
    elif opcion=="7":
        n1=int(input("ingresa el numero límite inferior de la lista: "))
        n2=int(input("ingresa el numero límite superior de la lista(numero grande): "))
        funcion_rango(n1,n2)
    elif opcion=="8":
        a=int(input("ingrese un número: "))
        b=int(input("ingrese otro número: "))
        mayor=numero_mayor(a,b)
        print("el mayor de los numeros ingresados es", mayor)
    elif opcion=="9":
        print("Gracias, hasta luego")
        break
    else: 
        input("esta opcion no es correcta")