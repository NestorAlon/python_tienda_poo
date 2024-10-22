class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        print(f"Productos en la categoría '{self.nombre}':")
        for i, producto in enumerate(self.productos):
                print(f"{i + 1}. {producto.nombre} - G{producto.precio: } (Talla: {producto.talla})")  