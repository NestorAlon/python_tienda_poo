class Carrito:
    def __init__(self):
        self.productos = [] 

    def agregar_al_carrito(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        return sum(producto.precio for producto in self.productos)

    def mostrar_carrito(self):
        if not self.productos:
            print("No hay productos en el carrito.")
        else:
            print("Productos en el carrito: ")
            for i, producto in enumerate(self.productos):
                print(f"{i + 1}. {producto.nombre} - G{producto.precio:} (Talla: {producto.talla})")