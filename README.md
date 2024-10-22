# python_tienda_poo
## Estructura del proyecto

El proyecto sigue una estructura modular que incluye clases para manejar los diferentes componentes de la tienda:

- **Producto**: Clase base para representar productos generales.
- **Camisa, Pantalon, Zapato**: Subclases de `Producto` que representan diferentes tipos de productos.
- **Categoria**: Clase que representa una categoría de productos.
- **Carrito**: Clase que gestiona la lógica del carrito de compras.
- **Tienda**: Clase que gestiona las categorías y los productos dentro de la tienda.

- ## Uso

Al ejecutar el programa, se presentan varias opciones para interactuar con la tienda:

1. **Ver categorías**: Muestra las diferentes categorías de productos disponibles en la tienda. Al seleccionar una categoría, se listan los productos dentro de ella.
2. **Ver carrito**: Muestra los productos que han sido añadidos al carrito de compras.
3. **Comprar**: Calcula el total de la compra, muestra el resumen y permite al usuario decidir si desea finalizar la compra o seguir comprando.
4. **Salir**: Termina el programa.
