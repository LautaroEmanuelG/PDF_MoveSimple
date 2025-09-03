# � PDF Content Shifter

Un script en Python para desplazar el contenido de archivos PDF en cualquier dirección.

## 🎯 Características

- ✅ Movimiento preciso en milímetros
- ✅ Control independiente de ejes X e Y
- ✅ Soporte para movimiento diagonal
- ✅ Procesamiento por lotes
- ✅ Interfaz simple y clara

## 🔧 Configuración de Direcciones

El script permite movimiento en ambos ejes:

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

| Configuración | Resultado                    |
| ------------- | ---------------------------- |
| `X=-4, Y=0`   | ← 4mm izquierda              |
| `X=3, Y=0`    | → 3mm derecha                |
| `X=0, Y=5`    | ↑ 5mm arriba                 |
| `X=0, Y=-2`   | ↓ 2mm abajo                  |
| `X=2, Y=3`    | ↗ Diagonal (derecha+arriba)  |
| `X=-2, Y=-2`  | ↙ Diagonal (izquierda+abajo) |

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
# Para mover 4mm a la izquierda (como solicitado originalmente)
DISPLACEMENT_X_MM = -4.0  # ← izquierda
DISPLACEMENT_Y_MM = 0.0   # sin movimiento vertical

# Para mover 3mm hacia arriba y 2mm a la derecha
DISPLACEMENT_X_MM = 2.0   # → derecha
DISPLACEMENT_Y_MM = 3.0   # ↑ arriba
```

### Paso 2: Colocar los PDFs

- Coloca tus archivos PDF en la carpeta `ToMove/`

### Paso 3: Ejecutar el Script

```bash
python pdf_mover_simple.py
```

### Paso 4: Recoger Resultados

- Los PDFs procesados estarán en `Processed/`

## 📂 Estructura del Proyecto

```
Script Mover PDFs/
├── ToMove/              # PDFs originales
├── Processed/           # PDFs procesados
├── config.py           # Configuración de movimiento
├── pdf_mover_simple.py # Script principal (sin emojis)
├── pdf_mover.py        # Script con interfaz visual
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

- **X positivo** = hacia la derecha →
- **X negativo** = hacia la izquierda ←
- **Y positivo** = hacia arriba ↑
- **Y negativo** = hacia abajo ↓

## ⚡ Versiones del Script

- **`pdf_mover_simple.py`**: Versión básica, compatible con cualquier terminal
- **`pdf_mover.py`**: Versión con emojis (requiere terminal compatible con Unicode)

## 🔍 Solución de Problemas

### Error de Codificación Unicode

Si ves errores como `UnicodeEncodeError`, usa la versión simple:

```bash
python pdf_mover_simple.py
```

### PDFs No Procesados

1. Verifica que los archivos estén en `ToMove/`
2. Confirma que son archivos PDF válidos
3. Revisa que tienes permisos de escritura en `Processed/`

## 📝 Notas Técnicas

- **Conversión**: 1mm = 2.834645 puntos PDF
- **Precisión**: Movimiento exacto al nivel de punto
- **Compatibilidad**: PyMuPDF 1.26.4+, Python 3.7+

---

🎯 **¡Tu solicitud original de "mover 4mm a la izquierda" está configurada por defecto!**
