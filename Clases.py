#Clase Categoria
class Categoria:
    def __init__(self, categoria_id, nombre):
        self.categoria_id = categoria_id
        self.nombre = nombre
        self.productos = [] #arreglo de productos
#Metodo para agregar productos al array
    def agregar_producto(self, producto):
        self.productos.append(producto)
#Clase Producto
class Producto:
    def __init__(self, producto_id, nombre, descripcion, precio, categoria):
        self.producto_id = producto_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.imagenes = [] #Se agrega un array de imagenes 
#metodo para agregar las imagenes a la clase producto
    def agregar_imagen(self, imagen):
        self.imagenes.append(imagen)
#clase imagen
class Imagen:
    def __init__(self, imagen_id, url, producto):
        self.imagen_id = imagen_id
        self.url = url #Se pide una para la imagen
        self.producto = producto

# Crear instancias de Categorias
categoria1 = Categoria(1, "Electrónicos") #se les asigna un producto y un id
categoria2 = Categoria(2, "Ropa")

# Crear instancias de Productos y asociarlos a Categorias
producto1 = Producto(101, "Laptop", "Potente laptop para trabajo", 1200.00, categoria1) #se crean un 
producto2 = Producto(102, "Camiseta", "Camiseta de algodón suave", 19.99, categoria2)

# Asociar productos a las categorías
categoria1.agregar_producto(producto1)
categoria2.agregar_producto(producto2)

# Crear instancias de Imagenes y asociarlas a Productos
imagen_producto1 = Imagen(1001, "SOY UN ENLACE", producto1)
imagen_producto2 = Imagen(1002, "SOY UN ENLACE", producto2)

# Asociar imágenes a los productos
producto1.agregar_imagen(imagen_producto1)
producto2.agregar_imagen(imagen_producto2)

# Acceder a la información de los objetos
print("Nombre del producto 1:", producto1.nombre)
print("Descripción del producto 1:", producto1.descripcion)
print("Categoría de producto 1:", producto1.categoria.nombre)
print("URL de la imagen del producto 1:", producto1.imagenes[0].url)
