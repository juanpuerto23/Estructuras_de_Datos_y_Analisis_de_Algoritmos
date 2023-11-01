plantilla_producto = "|{cod_producto}    |{nombre_producto}    |  {cantidad_producto}     |  {precio_unidad}  |  {iva} | {ivaTotal} | {valor_Total} |"

plantilla = f"""
    DATOS Y PROCESOS CORPORATIVOS LTDA

Facturas de ventas Nro. 10      Fecha: {{fecha}}
       Nit: 890090200-1 Regimen Comun
    Cliente: {{codigo_cliente}} - {{nombre_cliente}}

|Codigo |Nombre  |Cantidad|Vlr Unit|%Iva |Iva  |Vlr Total |
{{productos}}
                    Subtotal: ${{subtotal}}
                    Total Iva: ${{total_iva}}
                    Total Venta: ${{total_venta}}
"""

# Diccionario de elementos de la canasta basica

productos_data = {
    "001" : {"nombre": "Pescado", "precio_unitario": 2500, "porcentaje_iva": 15},
    "002" : {"nombre": "Carne", "precio_unitario": 5500, "porcentaje_iva": 35},
    "003" : {"nombre": "Papa", "precio_unitario": 4500, "porcentaje_iva": 25},
    "004" : {"nombre": "Arroz", "precio_unitario": 3000, "porcentaje_iva": 5},
    "005" : {"nombre": "Mora", "precio_unitario": 500, "porcentaje_iva": 45},
}

# Inicializar variables
subtotal = 0
total_iva = 0
total_venta = 0

# Datos pedidos
fecha = input("Ingrese la fecha actual: ")
cliente_codigo = input("Ingrese la cedula del Cliente: ")
cliente_nombre = input("Ingrese el nombre del Cliente: ")

productos_factura = []

while True:
    codigo_producto = input("Ingrese el código del producto (o 'fin' para terminar): ")
    if codigo_producto == 'fin':
        break

    if codigo_producto in productos_data:
        producto = productos_data[codigo_producto]
        nombre_producto = producto['nombre']
        precio_unidad = producto['precio_unitario']
        porcentaje_iva = producto['porcentaje_iva']
    else:
        print("No se encontro el codigo del producto que digitaste.")
        continue

    cantidad_producto = int(input("Ingrese la cantidad del producto: "))
    valor_total = precio_unidad * cantidad_producto

    # Calcular el iva
    iva = (porcentaje_iva / 100) * valor_total
    subtotal += valor_total
    total_iva += iva

    datos_producto = {
        "cod_producto": codigo_producto,
        "nombre_producto": nombre_producto,
        "cantidad_producto": cantidad_producto,
        "precio_unidad": precio_unidad,
        "iva": porcentaje_iva,
        "ivaTotal": iva,
        "valor_Total": valor_total
    }

    productos_factura.append(plantilla_producto.format(**datos_producto))

productos_generados = "\n".join(productos_factura)

total_venta = subtotal + total_iva

datos_factura = {
    "fecha": fecha,
    "codigo_cliente": cliente_codigo,
    "nombre_cliente": cliente_nombre,
    "productos": productos_generados,
    "subtotal": subtotal,
    "total_iva": total_iva,
    "total_venta": total_venta
}

factura_generada = plantilla.format(**datos_factura)

ruta_archivo = "facturaFinal.txt"
with open(ruta_archivo, "w") as archivo:
    archivo.write(factura_generada)
