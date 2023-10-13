class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio


def main():
    productos = {
        "0": Producto("Canada Dry", 7500.0),
        "1": Producto("Doritos", 6200.0),
        "2": Producto("Mortadela", 7400.0),
        "3": Producto("Arequipe", 4800.0),
        "4": Producto("Huevos", 17000.0)
    }

    total_venta = 0.0
    compras = []
    lista_compras = []

    print("Bienvenido a la tienda")
    print("------ ------ ------ -----")

    print("Menú Principal de productos:")
    for codigo, producto in productos.items():
        print(f"Código: {codigo}, Nombre: {producto.get_nombre()}, Precio: ${producto.get_precio()}")

    while True:
        codigo = input("Ingresa el código del producto que deseas añadir al carrito de compras (E para salir): ")

        if codigo == "E":
            break

        producto = productos.get(codigo)

        if producto is None:
            print("Código no válido. Introduce un código válido.")
            continue

        cantidad = int(input("Ingrese la cantidad a comprar: "))

        if cantidad <= 0:
            print("Cantidad no válida para procesar compra. Introduce una cantidad válida.")
            continue

        precio_unitario = producto.get_precio()
        sub_total = precio_unitario * cantidad
        total_venta += sub_total

        compra = f"Producto: {producto.get_nombre()}, Cantidad: {cantidad}, Subtotal: ${sub_total}"
        compras.append(compra)
        lista_compras.append(compra)

        print(f"Compra agregada al carrito de compras: {compra}")

    iva = total_venta * 0.19
    total_con_iva = total_venta + iva

    print("----- ----- ----- -----")
    print("Carrito de compras: ")
    print(f"Total de la venta (sin IVA): ${total_venta}")
    print(f"IVA: ${iva}")
    print(f"Total con IVA: ${total_con_iva}")
    print("----- ----- ----- -----")

    print("Compras realizadas:")
    for compra in reversed(compras):
        print(compra)

    print("----- ----- ----- -----")
    print("Detalles de la compra (primero en entrar, primero en salir): ")
    for compra in lista_compras:
        print(compra)


if __name__ == "__main__":
    main()