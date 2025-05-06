"""
--------------------------------------------------------------------------------------------------
Este script fue desarrollado por Alejandro Arellano Camacho para fines de evaluación técnica.
Uso no autorizado, distribución o implementacion en producción sin consentimiento
previo del autor esta prohibido.

Este script realiza las siguientes operaciones:
1. Carga datos de ventas de un CSV y datos de inventario desde un Excel
2. Realiza transformaciones y calculos sobre los datos
3. Genera análisis de categorias y productos con bajo inventario
4. Exporta los resultados a archivos en una carpeta llamada 'resultados'
5. Todo el proceso está encapsulado en funciones para su reutilización
 
Autor: Luis Alejandro Arellano Camacho    
Contacto: luis.alex.2711@gmail.com
Fecha de entrega: 02/05/2025
---------------------------------------------------------------------------------------------------
"""
    
import pandas as pd
import os
from pathlib import Path
from datetime import datetime
import sys

# Vigencia del script
fecha_limite = datetime(2025, 5, 10)
hoy = datetime.now()

if hoy > fecha_limite:
    print("Este script ha expirado y ya no puede ejecutarse. ")
    sys.exit()
    
    
def show_watermark():
    print("="*60)
    print("Este script es propiedad intelectual de Alejandro Arellano")
    print("Creado exclusivamente para evaluación técnica - NO USAR en producción.")
    print("="*60)
    
def cargar_datos(archivo_ventas= 'datos_ventas.csv', archivo_inventario='inventario.xlsx'):
    """

Carga los archivos de datos necesarios para el análisis

Args:
    archivo_ventas (str): Ruta del archivo CSV de ventas
    archivo_inventario (str): Ruta al archivo Excel de inventario

Returns:
    tuple: DataFrames de (ventas, inventario)
    """
    
    try:
        # Cargar datos de ventas
        ventas = pd.read_csv(archivo_ventas, parse_dates=['fecha'])
        
        # Cargar datos de inventario
        inventario = pd.read_excel(archivo_inventario)

        return ventas, inventario
    
    except FileNotFoundError as e:
        print(f"Error al cargar archivos:{e}")
        raise
    except Exception as e:
        print(f"Error inesperado al cargar datos: {e}")
        raise
    
def transformar_datos(ventas):
    """
    Realiza transformaciones y cálculos sobre los datos de ventas

    Args:
        ventas (DataFrame): Datos de ventas
    
    Returns:
        DataFrame: Datos de ventas transformados con columna de ingrese_total
    """
    
    try:
        # Calcular ingreso total por venta
        ventas['ingreso_total'] = ventas['cantidad'] * ventas['precio_unitario']
        
        return ventas
    
    except KeyError as e:
        print(f"Falta columna requerida en los datos {e}")
        raise
    except Exception as e:
        print(f"Error en transformación de datos {e}")
        raise
    
def analizar_ventas(ventas):
    """
    Agrrupa y analiza ventas por categoría

    Args:
        ventas (DataFrame): Datos de ventas transformados
        
    Returns:
        tuple: (DataFrame con resumen por categoría, porcentajes por categoría)
    """
    
    try:
        # Agrupar ventas por categoría
        resumen_categorias = ventas.groupby('categoria').agg(
            ingreso_total=('ingreso_total', 'sum'),
            num_ventas=('ingreso_total', 'count')).sort_values('ingreso_total', ascending=False)
        
        # Calcular porcentaje de ventas por categoría
        total_ventas = resumen_categorias['ingreso_total'].sum()
        resumen_categorias['porcentaje'] = (resumen_categorias['ingreso_total'] / total_ventas) * 100
        
        return resumen_categorias
    
    except Exception as e:
        print(f"Error en análisis de ventas: {e}")
        raise

def identificar_inventario_bajo(inventario, umbral=10):
    """
    Identifica productos con bajo inventario

    Args:
        inventario (DataFrame): Datos de inventario
        umbral (int): Cantidad minima para considerar bajo inventario
        
    Returns:
        DataFrame: Productos con inventario bajo el umbral
    """
    
    try:
        return inventario[inventario['cantidad_disponible'] < umbral].sort_values('cantidad_disponible')
    
    except Exception as e:
        print(f"Error al identificar inventario bajo: {e}")
        raise
    
def exportar_resultados(resumen_categorias, inventario_bajo, carpeta_resultados='resultados'):
    """
    Exporta los resultados del análisis a archivos

    Args:
        resumen_categorias (DataFrame): Resumen de ventas por categoría
        inventario_bajo (DataFrame): Productos con bajo inventario
        carpeta_resultados (str): Carpeta destino para los archivos llamada 'resultados'.
    """
    
    try:
        # Crear carpeta si no existe
        Path(carpeta_resultados).mkdir(exist_ok=True)
        
        # Exportar resumen de ventas
        resumen_categorias.to_csv(f'{carpeta_resultados}/resumen_ventas.csv')
        
        # Exportar inventario bajo
        inventario_bajo.to_excel(f'{carpeta_resultados}/inventario_bajo.xlsx', index=False)
        
        print(f"Resultados exportados correctanente a la carpeta '{carpeta_resultados}'")
        
    except Exception as e:
        print(f"Error al exportar resultados: {e}")
        raise
    
def generar_datos_ejemplo():
    """
    Genera datos de ejemplo para demostración cuando no existen los archivos de entrada
    
    Returns: 
        tuple: DataFrames de (ventas, inventario) de ejemplo
    """
    # Datos de ventas de ejemplo
    datos_ventas = {
        'fecha': pd.date_range(start='2023-01-01', periods=50),
        'producto': [f'Prod_{i%5+1}' for i in range(50)],  # 50 elementos
        'cantidad': [i%10+1 for i in range(50)],  # 50 elementos
        'precio_unitario': [10.5, 15.0, 8.0, 20.0, 12.5] * 10,  # 5*10=50 elementos
        'categoria': ['Electrónicos', 'Hogar'] * 25  # 2*25=50 elementos
    }
    # Datos de inventario
    datos_inventario = {
        'producto': ['Prod_1', 'Prod_2', 'Prod_3', 'Prod_4', 'Prod_5'],
        'cantidad_disponible': [15, 3, 8, 20, 5],
        'categoria': ['Electrónicos', 'Hogar', 'Electrónicos', 'Ropa', 'Hogar']
    }
    return pd.DataFrame(datos_ventas), pd.DataFrame(datos_inventario)

def proceso_automatizado(archivo_ventas='datos_ventas.csv', archivo_inventario='inventario.xlsx', generar_ejemplo=False):
    """
    Función principal que ejecuta todo el proceso de análisis

    Args:
        archivo_ventas (str):Ruta al archivo CSV de ventas 'datos_ventas.csv'.
        archivo_inventario (str): Ruta al archivo Excek de inventario 'inventario.xlsx'.
        generar_ejemplo (bool): Si es True, genera datos ejemplo cuando no existan los archivos
        
    Returns:
        tuple: (resumen_categorias, inventario_bajo) o None si hay errores.
    """
    
    try:
        print("Iniciando proceso de análisis...")
        
        # Cargar datos
        try:
            ventas, inventario = cargar_datos(archivo_ventas, archivo_inventario)
            
        except FileNotFoundError as e:
            if not generar_ejemplo:
                print(f"Error: {e}. Use generar_ejemplo=True para datos Fictios. ")
                
                return None, None 
            print("Generando datos ejemplo.... ")
            ventas, inventario = generar_datos_ejemplo()
            
        # Validar columnas
        columnas_requeridas_ventas = {'fecha', 'producto', 'cantidad', 'precio_unitario', 'categoria'}
        if not columnas_requeridas_ventas.issubset(ventas.columns):
            print("Error: El archivo de ventas no tiene las columnas requeridas. ")
            
            return None, None   
            
        # Transformar y analizar
        ventas = transformar_datos(ventas)
        resumen_categorias = analizar_ventas(ventas)
        inventario_bajo = identificar_inventario_bajo(inventario)
        
        
        # Exportar resultados
        exportar_resultados(resumen_categorias, inventario_bajo)
        
        show_watermark()
        
        print("¡Proceso completado exitosamente!")
        
        return resumen_categorias, inventario_bajo
    
    except Exception as e:
        print(f"Error critico: {str(e)}")
        return None, None
    
if __name__ == "__main__":
    # Ejecutar el proceso automáticamente al correr el script
    # Si los archivos no existen, generará datos ejemplo
    proceso_automatizado(generar_ejemplo=True)