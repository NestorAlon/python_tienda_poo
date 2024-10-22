

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.categorias = [] 

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def listar_categorias(self):
        return self.categorias 
