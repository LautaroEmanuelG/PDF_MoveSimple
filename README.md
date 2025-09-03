# 📄 PDF Content Shifter - PROBLEMA RESUELTO ✅

Un script en Python para desplazar el contenido de archivos PDF en cualquier dirección.

## 🎯 Características

- ✅ Movimiento preciso en milímetros
- ✅ Control independiente de ejes X e Y
- ✅ Soporte para movimiento diagonal
- ✅ Procesamiento por lotes
- ✅ **Mantiene calidad vectorial original**
- ✅ **PROBLEMA ORIGINAL SOLUCIONADO**

## 🚨 PROBLEMA IDENTIFICADO Y RESUELTO

### ❌ Errores del Script Original:

1. **Uso de API privada incorrecta**: `fitz.TOOLS._insert_contents()`
2. **Parámetros inexistentes**: `alpha` en `show_pdf_page()`
3. **Métodos que fallaban**: `set_contents()` con error "bad xref"
4. **Formato de datos incorrecto**: Error en procesamiento de dibujos vectoriales

### ✅ Solución Implementada:

**Nueva implementación usando `show_pdf_page` correctamente:**

```python
# Método que SÍ funciona y mantiene calidad vectorial
dest_page.show_pdf_page(
    dest_rect,     # rectángulo con desplazamiento
    source_doc,    # documento fuente
    page_num,      # página fuente
    clip=None,     # sin recorte
    rotate=0,      # sin rotación
    oc=0,          # sin contenido opcional
    overlay=True,  # en primer plano
    keep_proportion=True  # mantener proporción
)
```

## 🔧 Configuración de Direcciones

### Eje X (Horizontal)

```python
DISPLACEMENT_X_MM = 4.0   # → Mover 4mm hacia la DERECHA
DISPLACEMENT_X_MM = -4.0  # ← Mover 4mm hacia la IZQUIERDA
```

### Eje Y (Vertical)

```python
DISPLACEMENT_Y_MM = 3.0   # ↑ Mover 3mm hacia ARRIBA
DISPLACEMENT_Y_MM = -3.0  # ↓ Mover 3mm hacia ABAJO
```

### 💡 Ejemplos Prácticos

| Configuración | Resultado                                |
| ------------- | ---------------------------------------- |
| `X=-10, Y=10` | ← 10mm izquierda, ↑ 10mm arriba (actual) |
| `X=-4, Y=0`   | ← 4mm izquierda                          |
| `X=3, Y=0`    | → 3mm derecha                            |
| `X=0, Y=5`    | ↑ 5mm arriba                             |
| `X=0, Y=-2`   | ↓ 2mm abajo                              |

## 📚 Instalación

1. **Instalar PyMuPDF:**

```bash
pip install PyMuPDF
```

2. **Verificar instalación:**

```bash
python -c "import fitz; print('PyMuPDF instalado correctamente')"
```

## 🚀 Uso

### Paso 1: Configurar el Movimiento

Edita `config.py` y ajusta los valores:

```python
# Configuración actual (10mm izquierda, 10mm arriba)
DISPLACEMENT_X_MM = -10.0  # ← izquierda
DISPLACEMENT_Y_MM = 10.0   # ↑ arriba
```

### Paso 2: Colocar los PDFs

- Coloca tus archivos PDF en la carpeta `ToMove/`

### Paso 3: Ejecutar el Script CORREGIDO

```bash
python pdf_mover_simple.py
```

### Paso 4: Recoger Resultados

- Los PDFs procesados estarán en `Processed/`

## 📂 Estructura del Proyecto

```
PDF_MoveSimple/
├── ToMove/              # PDFs originales
├── Processed/           # PDFs procesados
├── config.py           # Configuración de movimiento
├── pdf_mover_simple.py # ✅ Script principal CORREGIDO
├── pdf_mover_simple_v2.py    # Versión alternativa (método raster)
├── pdf_mover_hybrid.py       # Versión híbrida
└── README.md           # Este archivo
```

## 🎨 Sistema de Coordenadas

```
    ↑ Y positivo (arriba)
    |
────┼──── → X positivo (derecha)
    |
    ↓ Y negativo (abajo)

X negativo (izquierda)
```

## 🔍 Estado de Errores (ANTES vs DESPUÉS)

### ❌ ANTES (No funcionaba):

```
Error procesando ejemplo.pdf: show_pdf_page() got an unexpected keyword argument 'alpha'
AttributeError: 'Page' object has no attribute '_insert_contents'
Error con transformación de contenido: bad xref
```

### ✅ DESPUÉS (Funciona perfectamente):

```
PDF CONTENT SHIFTER
========================================
Desplazamiento: X=-10.0mm, Y=10.0mm

Procesando: ejemplo.pdf
Completado: ejemplo.pdf
Procesando: Pagan Atras 2 mover 4 mm.pdf
Completado: Pagan Atras 2 mover 4 mm.pdf

Procesados: 2/2
Completado exitosamente!
```

## ⚡ Versiones Disponibles

1. **`pdf_mover_simple.py`**: ✅ **PRINCIPAL CORREGIDA** - Usa `show_pdf_page` (vectorial)
2. **`pdf_mover_simple_v2.py`**: Método raster (como respaldo)
3. **`pdf_mover_hybrid.py`**: Híbrida (vectorial con fallback)

## 🔬 Análisis Técnico del Problema

### Problema Raíz:

- El script original usaba métodos internos/privados de PyMuPDF incorrectamente
- Los parámetros pasados a `show_pdf_page` no coincidían con la API real
- La transformación de contenido PDF se hacía de manera incorrecta

### Solución:

- **Migración a API pública**: Uso correcto de `show_pdf_page`
- **Parámetros válidos**: Solo usar parámetros documentados oficialmente
- **Método vectorial**: Mantiene calidad original sin rasterización

## 📝 Notas Técnicas

- **Conversión**: 1mm = 2.834645 puntos PDF
- **Método**: `show_pdf_page` para calidad vectorial perfecta
- **API**: Uso exclusivo de métodos públicos de PyMuPDF
- **Compatibilidad**: PyMuPDF 1.23.0+, Python 3.7+

---

## 🎉 RESULTADO FINAL

**✅ EL SCRIPT AHORA FUNCIONA CORRECTAMENTE**

- ✅ Mueve el contenido exactamente según la configuración
- ✅ Mantiene la calidad vectorial original
- ✅ Procesa todos los archivos sin errores
- ✅ Usa API pública y estable de PyMuPDF

🎯 **El problema ha sido completamente resuelto. El script ahora desplaza correctamente el contenido de los PDFs según los milímetros especificados en `config.py`**
