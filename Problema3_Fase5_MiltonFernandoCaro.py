# Nombre: Milton Fernando Caro Fraile
# Programa: Ingeniería de Sistemas
# Curso: Fundamentos de Programación
# Grupo: 512
# Zona Centro Boyacá Cead Chiquinquirá

# Formato:
# [Código del artículo, Nombre del artículo, Stock actual, Stock mínimo requerido]

inventario = [
    ["A001", "Teclado mecánico", 4, 10],
    ["A002", "Mouse inalámbrico", 15, 10],
    ["A003", "Cable HDMI", 8, 8],
    ["A004", "Monitor 24 pulgadas", 2, 6],
    ["A005", "Memoria USB 64GB", 25, 12],
    ["A006", "Disco duro externo 1TB", 5, 5],
    ["A007", "Auriculares con micrófono", 3, 7],
    ["A008", "Webcam HD", 0, 4],
    ["A009", "Impresora láser", 1, 3],
    ["A010", "Router Wi-Fi", 6, 6]
]

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Calcula la cantidad que se debe pedir para reabastecer un artículo.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

def mostrar_reporte_reabastecimiento(matriz_inventario):
    """
    Muestra el nombre del artículo y la cantidad que debe solicitarse.
    """
    print("=== REPORTE DE REABASTECIMIENTO ===")

    for articulo in matriz_inventario:
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        print("-------")

        cantidad_pedir = calcular_cantidad_a_pedir(
            stock_actual,
            stock_minimo
        )

        print(f"Artículo: {nombre} | Cantidad a pedir: {cantidad_pedir}")

# Programa principal
mostrar_reporte_reabastecimiento(inventario)