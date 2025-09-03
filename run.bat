@echo off
echo.
echo 🔧 PDF Content Mover
echo ===================
echo.

REM Verificar que Python esté disponible
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no encontrado. Ejecuta install.bat primero.
    pause
    exit /b 1
)

REM Verificar que existe la carpeta ToMove
if not exist "ToMove" (
    echo 📁 Creando carpeta ToMove...
    mkdir ToMove
    echo ⚠️ Coloca tus archivos PDF en la carpeta ToMove y ejecuta este script nuevamente.
    pause
    exit /b 0
)

REM Ejecutar el script principal
echo 🚀 Ejecutando PDF Content Mover...
echo.
python pdf_mover.py

echo.
echo ✅ Proceso completado. Presiona cualquier tecla para salir.
pause >nul
