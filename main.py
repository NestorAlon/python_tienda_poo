from clases.Producto import Camisa, Pantalon, Zapato
from clases.Carrito import Carrito
from clases.Categoria import Categoria
from clases.Tienda import Tienda

def main():

    tienda = Tienda("Tienda POO")

    ropa_hombre = Categoria("Ropa de Hombre")
    ropa_mujer = Categoria("Ropa de Mujer")

    camisa_hombre = Camisa("Camisa Calvin Klein", 750.000, 4, "M", "Larga")
    pantalon_hombre = Pantalon("Pantalón Levis", 450.000, 3, "L", "Recto")
    zapato_hombre = Zapato("Nike air force 1", 950.000, 5, "42", "Casual")

    camisa_mujer = Camisa("Camisa Zara", 250.000, 10, "S", "Corta")
    pantalon_mujer = Pantalon("Pantalón Levis", 400.000, 5, "M", "Ancho")
    zapato_mujer = Zapato("Nike air max", 760.000, 9, "38", "Deportivo")

    ropa_hombre.agregar_producto(camisa_hombre)
    ropa_hombre.agregar_producto(pantalon_hombre)
    ropa_hombre.agregar_producto(zapato_hombre)

    ropa_mujer.agregar_producto(camisa_mujer)
    ropa_mujer.agregar_producto(pantalon_mujer)
    ropa_mujer.agregar_producto(zapato_mujer)

    tienda.agregar_categoria(ropa_hombre)
    tienda.agregar_categoria(ropa_mujer)

    carrito = Carrito()

    while True:
        print("\nBienvenido a", tienda.nombre)
        print("1. Ver categorías")
        print("2. Ver carrito")
        print("3. Comprar")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion.isdecimal():
            opcion = int(opcion)

            if opcion == 1:

                categorias = tienda.listar_categorias()
                for i, categoria in enumerate(categorias):
                    print(f"{i + 1}. {categoria.nombre}")

                while True:
                    try:
                        categoria_opcion = int(input("Seleccione una categoría: "))
                        break
                    except ValueError:
                        print("Ingrese solamente numeros")
                
                categoria_seleccionada = categorias[categoria_opcion - 1]
                categoria_seleccionada.listar_productos()  

                while True:
                    try:
                        producto_opcion = int(input("Seleccione un producto para agregar al carrito: "))
                        break
                    except ValueError:
                        print("Ingrese solamente numeros")
                
                producto_seleccionado = categoria_seleccionada.productos[producto_opcion - 1]

                carrito.agregar_al_carrito(producto_seleccionado)
                print(f"{producto_seleccionado.nombre} añadido al carrito")

            elif opcion == 2:
                carrito.mostrar_carrito()

            elif opcion == 3:
                carrito.mostrar_carrito()             
                total = carrito.calcular_total()
                print(f"El total de su compra es: G{total: }")
                print("Ingrese 1 si quiere finalizar su compra")
                print("Ingrese 2 si quiere seguir comprando")
                while True:
                    try:
                        compra_opcion = int(input("Seleccione una opcion: "))
                        break
                    except ValueError:
                        print("Ingrese solamente numeros")
                if compra_opcion == 1:
                    print("Compra completada con exito.")
                else:
                    continue
                carrito = Carrito() 
                continue  

            elif opcion == 4:
                print("Gracias por la visita.")
                break
            else:
                print("Seleccione una opcion valida")

       

        else:
            print("Ingrese un numero del 1 al 4")


main()