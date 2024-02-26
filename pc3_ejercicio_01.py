#Ejercicio 01
# Una tienda de autopartes necesita un programa para catalogar sus productos,crear la clase catalogo
# y producto, realizar un objeto dentro de un catalgo de productos el cual debe tener un metodo para agregar
# productos el cual debe tener un metodo para agregar productos y otra para mostrar toda la lista de productos.

class Producto:
    nombre:None
    precio:None
    marca:None
    def __init__(self,nombre,precio,marca):
        self.nombre=nombre
        self.precio=precio
        self.marca=marca  
        print(f"se ha creado el producto {self.nombre}")
    def __str__(self):
        return f"producto {self.nombre} con precio {self.precio} de la marca {self.marca}"

class Catalogo:
    productos=[]
    def __init_(self, productos=[]):
        self.productos=productos
    def agregarProducto(self,p): 
        self.productos.append(p)
    def mostrarListaDeProductos(self):
        for i, p in enumerate(self.productos):
            print(i+1,p)

##verificamos que las clases creadas operen correctamente 
producto1=Producto("llanta",50,"michelin")
producto2=Producto("bateria",145,"energizer")
print(producto1)
print(producto2)

catalogo1=Catalogo()
catalogo1.agregarProducto(producto1)
catalogo1.agregarProducto(producto2)
catalogo1.mostrarListaDeProductos()
