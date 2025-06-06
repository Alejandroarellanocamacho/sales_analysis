 # Proyecto: Análisis de ventas e Inventario 📊

 ## Descripción del Proyecto

 Este Proyecto automatiza el análisis de datos de ventas e inventario para identificar:

- **Patrones de ventas** por categoría de productos

- **Productos con bajo inventario** (según un umbral configurable).

- Genera reportes listos para el analisis y toma de decisiones.

# 🔧 Instalación y Uso 

**Requisitos**

- Python 3.8+
- Librerias pandas, openpuxli

instala dependencias:

```
pip install pandas openpyxl
```

**Ejecución**

```
python src/sales_analysis.py
```

Opcienes:

- 'archivo_ventas': Ruta personalizada para el CSV de ventas.
- ´archivo_inventario´: Ruta personalizada para el Excel de inventario.
- 'generar_ejemplo': Genera datos ficticios si no hay archivos de entrada.

# Funcionalidades Clave

1. **Carga de datos**
    - Soporta CSV (ventas) y Excel (inventario).
    - Genera datos ejemplo si no existen los archivos.
2. **Análisis:**
    - Agrupa ventas por categoría y calcula ingresos totales.
    - Identifica productos con inventario baho (umbral ajustable).
3. **Exportación**
    - Guarda resultados en *resultados/(CSV y Excel)*
4. **Seguridad**
    - Bloqueo de ejecución después de fecha límite.
    - Mensajes de advertencia sobre uso no autorizado.

# Ejemplo de Salida

Iniciando proceso de análisis...
Generando datos ejemplo...
¡Proceso completado exitosamente!
============================================================
Este script es propiedad intelectual de Alejandro Arellano
Creado exclusivamente para evaluación técnica - NO USAR en producción.
============================================================

# Autor y Licencia

- **Autor**: Luis Alejandro Arellano Camacho
- **Contacto**: luis.alex.2711@gmail.com
- **Fecha de entrega**: 02/05/2025
- **Licencia**: Uso restringido para evalucación técnica, Prohibida su distribución o implementación e4n producción sin autorización.

# Roadmap

- Integración con bases de datos (SQL, BigQuery)
- Dashboard interactivo (Power Bi/Looker Studio)
- Alertas automaticás por email para inventario bajo.

✨ **¡Contribucuines y feedback son biemvenidos** ✨
*Actualizado*: Mayo 2025
