class Categoria: #Clase categoria.
    def __init__(self, categoria_id, nombre):
        self.categoria_id = categoria_id
        self.nombre = nombre

class Producto: #Clase Producto
    def __init__(self, producto_id, nombre, descripcion, precio, categoria):
        self.producto_id = producto_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria

class Imagen: #Clase imagen
    def __init__(self, imagen_id, url, producto):
        self.imagen_id = imagen_id
        self.url = url
        self.producto = producto

# Crear instancias de Categorias
categoria1 = Categoria(1, "Electrónicos")
categoria2 = Categoria(2, "Ropa")

# Crear instancias de Productos
producto1 = Producto(101, "Laptop", "Potente laptop para trabajo", 1200.00, categoria1)
producto2 = Producto(102, "Camiseta", "Camiseta de algodón suave", 19.99, categoria2)

# Crear instancias de Imagenes asociadas a Productos
imagen_producto1 = Imagen(1001, "https://soy un url.jpg", producto1)
imagen_producto2 = Imagen(1002, "https://soy un url.jpg", producto2)

# Acceder a la información de los objetos

#CLASE PRUEBA
print("Nombre del producto 1:", producto1.nombre)
print("Descripción del producto :", producto1.descripcion)
print("Categoría de producto 1:", producto1.categoria.nombre)
print("URL de la imagen del producto 1:", imagen_producto1.url)
