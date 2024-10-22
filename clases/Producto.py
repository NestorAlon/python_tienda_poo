class Producto:
    def __init__(self, nombre, precio, cantidad, talla):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.talla = talla
    
    def mostrar_precio(self):
        print(f"Precio de {self.nombre}: ${self.precio:}")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:}")
        print(f"Cantidad disponible: {self.cantidad}")
        print(f"Talla: {self.talla}")

class Camisa(Producto):
    def __init__(self, nombre, precio, cantidad, talla, manga):
        super().__init__(nombre, precio, cantidad, talla)
        self.manga = manga

    def mostrar_informacion(self):
        super().mostrar_informacion()  # Llama al método de la clase padre
        print(f"Tipo de manga: {self.manga}")


class Pantalon(Producto):
    def __init__(self, nombre, precio, cantidad, talla, tipoCorte):
        super().__init__(nombre, precio, cantidad, talla)
        self.tipoCorte = tipoCorte

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo de corte: {self.tipoCorte}")

class Zapato(Producto):
    def __init__(self, nombre, precio, cantidad, talla, tipoZapato ):
        super().__init__(nombre, precio, cantidad, talla)
        self.tipoZapato = tipoZapato

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo de zapato: {self.tipoZapato}")

