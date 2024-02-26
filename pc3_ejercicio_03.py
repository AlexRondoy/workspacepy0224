#Ejercicio 03 
#Del siguiente texto realizar al menos 4 funciones de string

texto="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

##creamos una función que me permita saber cuántas veces se repite una palabra en el exto 
def ocurrencias(palabra:str):
    palabra_por_buscar=palabra.lower()
    texto_principal=texto.lower()
    numero_ocurrecias= texto_principal.count(palabra_por_buscar)
    return f"la palabra {palabra} se repite {numero_ocurrecias} veces en el texto"

lorem=ocurrencias("Lorem")
print(lorem)

##creamos una función que se encargue de reemplazar una palabra existente por otra palabra nueva que indicaremos
def reemplazar_palabra(palabra_existente:str,nueva_palabra:str):
    if palabra_existente in texto: 
        return texto.replace(palabra_existente,nueva_palabra)
    else: 
        print("esta palabra no forma parte del texto")
            
Ipsum=reemplazar_palabra("Ipsum","Castillo")
print(Ipsum)

##creamos una función que tenga como funcionalidad contar la cantidad de palabras de un texto 
def contar_palabras(texto):
    lista=texto.split(" ")
    cantidad=len(lista)
    return f"el texto tiene {cantidad} palabras"
prueba=contar_palabras(texto)
print(prueba)

##definimos una función que permita ingresar una palabra, verificar si está en el texto y luego convertirla en mayúscula 
def convertir_en_mayuscula(palabra:str):
    try:
        if palabra in texto:
            palabra_mayuscula=palabra.upper()
            new_text=texto.replace(palabra,palabra_mayuscula)
            print(new_text)
    except:
        print("la palabra ingresada no se encuentra en el texto") 
industry=convertir_en_mayuscula("industry")
print(industry)