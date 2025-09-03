# 📄 PDF Content Shifter - Desplazamiento Inteligente

## 🎯 Descripción

Herramienta avanzada para desplazar contenido de archivos PDF manteniendo la orientación original. **Soluciona el problema de rotación involuntaria** mediante compensación automática según la rotación de cada página.

## ✨ Características Principales

- ✅ **Detección automática de rotación** de página (0°, 90°, 180°, 270°)
- ✅ **Compensación inteligente** de coordenadas según rotación PDF
- ✅ **Preservación total** de orientación visual original
- ✅ **Sin rotación involuntaria** del contenido
- ✅ Soporte para páginas verticales y horizontales
- ✅ Configuración simple en milímetros
- ✅ Conversión automática mm → puntos PDF

## 🚀 Uso Rápido

1. **Coloca tus PDFs** en la carpeta `ToMove/`
2. **Configura el desplazamiento** en `config.py`
3. **Ejecuta** el script:
   ```bash
   python pdf_mover_simple.py
   ```
4. **Obtén los resultados** en la carpeta `Processed/`

## ⚙️ Configuración

Edita el archivo `config.py` para ajustar el desplazamiento:

```python
# Mover 4mm hacia la derecha
DISPLACEMENT_X_MM = 4.0
DISPLACEMENT_Y_MM = 0.0
```

### 📐 Ejemplos de Configuración

| Objetivo                       | DISPLACEMENT_X_MM | DISPLACEMENT_Y_MM |
| ------------------------------ | ----------------- | ----------------- |
| 🏃‍➡️ Mover 3mm a la derecha   | `3.0`             | `0.0`             |
| ⬆️ Mover 2mm hacia arriba      | `0.0`             | `2.0`             |
| ↖️ Mover diagonal (izq-arriba) | `-2.0`            | `1.5`             |
| ↘️ Mover diagonal (der-abajo)  | `2.0`             | `-1.5`            |
| 🚫 Sin movimiento              | `0.0`             | `0.0`             |

### 🧭 Sistema de Coordenadas

```
     ↑ Y positivo (arriba)
     |
← ---+--- → X positivo (derecha)
     |
     ↓ Y negativo (abajo)
```

## 📁 Estructura de Carpetas

```
PDF_MoveSimple/
├── ToMove/          # 📂 PDFs originales aquí
├── Processed/       # 📂 PDFs procesados aquí
├── config.py        # ⚙️ Configuración
├── pdf_mover_simple.py  # 🔧 Script principal
└── README.md        # 📖 Esta documentación
```

## 🛠️ Instalación

### Requisitos

- Python 3.7+
- PyMuPDF (fitz)

### Instalación rápida

```bash
pip install -r requirements.txt
```

O manualmente:

```bash
pip install PyMuPDF
```

## 💡 Casos de Uso Comunes

### 🖨️ **Ajuste para Impresión**

```python
# Compensar desalineación de impresora
DISPLACEMENT_X_MM = 2.0  # 2mm derecha
DISPLACEMENT_Y_MM = -1.0 # 1mm abajo
```

### 📐 **Ajuste de Márgenes**

```python
# Aumentar margen izquierdo
DISPLACEMENT_X_MM = 5.0  # 5mm derecha
DISPLACEMENT_Y_MM = 0.0
```

### 🎮 **Ajuste para Juegos de Mesa**

```python
# Compensar corte de cartas
DISPLACEMENT_X_MM = 1.5
DISPLACEMENT_Y_MM = 1.5
```

## 🔧 Configuración Avanzada

En `config.py` también puedes ajustar:

```python
# Calidad de compresión (0-4, 4 = máxima)
COMPRESSION_LEVEL = 3

# Usar compresión deflate
USE_DEFLATE = True

# Carpetas personalizadas
INPUT_FOLDER = "MisPDFs"
OUTPUT_FOLDER = "Resultados"
```

## 📊 Características Técnicas

- **Precisión**: 0.1mm (limitado por resolución PDF)
- **Formatos soportados**: PDF
- **Preserva**: Calidad vectorial, texto seleccionable, metadatos
- **Velocidad**: ~100 páginas/minuto (aproximado)
- **Limitaciones**: El contenido que se salga de la página se recortará

## 🐛 Solución de Problemas

### ❓ **El contenido desaparece**

**Causa**: Se movió fuera de los límites de la página  
**Solución**: Usar valores de desplazamiento menores

### ❓ **No se ven cambios**

**Causa**: Desplazamiento configurado en 0.0  
**Solución**: Verificar valores en `config.py`

### ❓ **Error de permisos**

**Causa**: Archivo PDF abierto en otro programa  
**Solución**: Cerrar el PDF antes de procesarlo

### ❓ **Error al instalar PyMuPDF**

**Solución**:

```bash
pip install --upgrade pip
pip install PyMuPDF
```

## 📝 Registro de Cambios

### v2.0 - Versión Mejorada

- ✨ Mantiene tamaño de página original
- ✨ Sin rotación ni deformación del contenido
- ✨ Configuración más clara
- ✨ Mejor manejo de errores
- ✨ Documentación mejorada

### v1.0 - Versión Original

- ✅ Funcionalidad básica de desplazamiento

## 📄 Licencia

Software libre para uso personal y comercial.

## 🤝 Contribuciones

¡Las mejoras son bienvenidas! Abre un issue o pull request.

---

**💡 Tip**: Para mejores resultados, haz una copia de respaldo de tus PDFs originales antes de procesarlos.
