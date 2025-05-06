import pandas as pd
import matplotlib.pyplot as plt

# Función para cargar datos de ventas desde un archivo CSV
def cargar_datos_ventas(nombre_archivo):
    try:
        datos = pd.read_csv(nombre_archivo)
        print("Datos de ventas cargados correctamente.")
        return datos
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return None

# Función para analizar ventas por producto
def analizar_ventas_por_producto(datos): 
    if 'producto' not in datos.columns or 'cantidad' not in datos.columns:
        print("Error: Las columnas 'producto' y/o 'cantidad' no existen en los datos.")
        return None
    resumen = datos.groupby('producto')['cantidad'].sum().sort_values(ascending=False)
    return resumen

# Función para graficar ventas por producto
def graficar_ventas(resumen_ventas):
    if resumen_ventas is None or resumen_ventas.empty:
        print("No hay datos para graficar.")
        return
    resumen_ventas.plot(kind='bar', color='skyblue')
    plt.title("Ventas por Producto")
    plt.xlabel("Producto")
    plt.ylabel("Cantidad Vendida")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Función para identificar inventario bajo
def identificar_inventario_bajo(inventario, umbral=10):
    if 'producto' not in inventario.columns or 'cantidad_disponible' not in inventario.columns:
        print("Error: Las columnas necesarias no están en el inventario.")
        return None
    return inventario[inventario['cantidad_disponible'] < umbral]

# Función para generar datos de ejemplo de ventas
def generar_datos_ejemplo():
    datos = {
        'producto': [f'Prod_{i}' for i in range(1, 51)],
        'cantidad': [(i % 10) + 1 for i in range(50)],
        'precio_unitario': [round(5 + i * 0.5, 2) for i in range(50)],
        'fecha': pd.date_range(start='2024-01-01', periods=50, freq='D')
    }
    return pd.DataFrame(datos)

# Función para generar inventario de ejemplo
def generar_inventario_ejemplo():
    datos_inventario = {
        'producto': ['Prod_1', 'Prod_2', 'Prod_3', 'Prod_4', 'Prod_5'],
        'cantidad_disponible': [15, 3, 8, 20, 10],
        'categoria': ['Electronicos', 'Hogar', 'Tecnologia', 'Ropa', 'Accesorios']
    }
    return pd.DataFrame(datos_inventario)

# Código principal
if __name__ == "__main__":
    # Generar datos de ejemplo
    ventas = generar_datos_ejemplo()
    inventario = generar_inventario_ejemplo()

    # Analizar y graficar ventas
    resumen_ventas = analizar_ventas_por_producto(ventas)
    if resumen_ventas is not None:
        print("\nResumen de ventas por producto:\n", resumen_ventas)
        graficar_ventas(resumen_ventas)

    # Identificar inventario bajo
    inventario_bajo = identificar_inventario_bajo(inventario)
    if inventario_bajo is not None and not inventario_bajo.empty:
        print("\nProductos con inventario bajo:\n", inventario_bajo)
    else:
        print("\nNo se encontraron productos con inventario bajo.")
