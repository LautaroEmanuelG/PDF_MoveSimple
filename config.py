#!/usr/bin/env python3
"""
⚙️ Configuración del PDF Content Shifter
========================================

Archivo de configuración para personalizar el comportamiento del script.
Todos los valores son en milímetros (mm) para facilitar las mediciones.
"""

# 📏 DESPLAZAMIENTO DEL CONTENIDO
# =====================================

# 🔄 DESPLAZAMIENTO HORIZONTAL (eje X)
# Positivo = hacia la DERECHA (→)
# Negativo = hacia la IZQUIERDA (←)
# Valor en milímetros (mm)
DISPLACEMENT_X_MM = 0.0

# 🔄 DESPLAZAMIENTO VERTICAL (eje Y)
# Positivo = hacia ARRIBA (↑)
# Negativo = hacia ABAJO (↓)
# Valor en milímetros (mm)
DISPLACEMENT_Y_MM = -4.0

# 💡 EJEMPLOS DE CONFIGURACIÓN:
# =============================
# Para mover 3mm a la derecha:          DISPLACEMENT_X_MM = 3.0,  DISPLACEMENT_Y_MM = 0.0
# Para mover 2mm hacia arriba:          DISPLACEMENT_X_MM = 0.0,  DISPLACEMENT_Y_MM = 2.0
# Para mover 5mm izquierda, 3mm abajo:  DISPLACEMENT_X_MM = -5.0, DISPLACEMENT_Y_MM = -3.0
# Para diagonal (derecha-arriba):       DISPLACEMENT_X_MM = 2.0,  DISPLACEMENT_Y_MM = 1.5
# Sin movimiento:                       DISPLACEMENT_X_MM = 0.0,  DISPLACEMENT_Y_MM = 0.0

# 📁 DIRECTORIOS
# ==============

# Carpeta donde están los PDFs originales
INPUT_FOLDER = "ToMove"

# Carpeta donde se guardarán los PDFs procesados
OUTPUT_FOLDER = "Processed"

# 🎯 CONFIGURACIONES PREDEFINIDAS COMUNES
# =======================================
# Descomente la configuración que necesite y comente las variables de arriba

# # Configuración: Mover hacia la derecha 4mm (común para imprenta)
# DISPLACEMENT_X_MM = 4.0
# DISPLACEMENT_Y_MM = 0.0

# # Configuración: Mover hacia arriba 3mm
# DISPLACEMENT_X_MM = 0.0
# DISPLACEMENT_Y_MM = 3.0

# # Configuración: Ajuste diagonal común
# DISPLACEMENT_X_MM = 2.0
# DISPLACEMENT_Y_MM = 2.0

# # Configuración: Sin desplazamiento (para pruebas)
# DISPLACEMENT_X_MM = 0.0
# DISPLACEMENT_Y_MM = 0.0

# 📋 NOTAS IMPORTANTES:
# ====================
# - Los valores son en milímetros (mm) para mayor precisión
# - El script convierte automáticamente a puntos PDF (1mm ≈ 2.83 puntos)
# - Los desplazamientos positivos mueven el contenido hacia la derecha/arriba
# - Los desplazamientos negativos mueven el contenido hacia la izquierda/abajo
# - El tamaño de la página NO cambia, solo se mueve el contenido
# - Si el contenido se sale de los límites de la página, se recortará

# 🔧 CONFIGURACIÓN AVANZADA (para usuarios expertos)
# ==================================================

# Factor de conversión mm a puntos PDF (NO MODIFICAR salvo casos muy específicos)
MM_TO_POINTS = 2.834645

# Calidad de compresión del PDF resultante (0-4, donde 4 es máxima compresión)
COMPRESSION_LEVEL = 3

# Usar deflate para reducir tamaño de archivo
USE_DEFLATE = True
