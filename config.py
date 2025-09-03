#!/usr/bin/env python3
"""
⚙️ Configuración del PDF Content Shifter
========================================

Archivo de configuración para personalizar el comportamiento del script.
"""

# 📏 DESPLAZAMIENTO DEL CONTENIDO
# =====================================

# 🔄 DESPLAZAMIENTO HORIZONTAL (eje X)
# Positivo = hacia la DERECHA (→)
# Negativo = hacia la IZQUIERDA (←)
DISPLACEMENT_X_MM = -10.0

# 🔄 DESPLAZAMIENTO VERTICAL (eje Y)
# Positivo = hacia ARRIBA (↑)
# Negativo = hacia ABAJO (↓)
DISPLACEMENT_Y_MM = 10.0

# 💡 EJEMPLOS:
# Para mover 3mm a la derecha: DISPLACEMENT_X_MM = 3.0
# Para mover 2mm hacia arriba: DISPLACEMENT_Y_MM = 2.0
# Para mover diagonal: DISPLACEMENT_X_MM = -2.0, DISPLACEMENT_Y_MM = 1.5

# 📁 DIRECTORIOS
# Carpeta donde están los PDFs originales
INPUT_FOLDER = "ToMove"

# Carpeta donde se guardarán los PDFs procesados
OUTPUT_FOLDER = "Processed"
