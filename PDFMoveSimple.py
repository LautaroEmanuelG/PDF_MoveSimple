#!/usr/bin/env python3
"""
PDF Content Shifter - Simple Version
===================================

Script simplificado para mover contenido de PDFs sin problemas de codificación.
"""

import sys
import fitz
from pathlib import Path
from config import DISPLACEMENT_X_MM, DISPLACEMENT_Y_MM, INPUT_FOLDER, OUTPUT_FOLDER


class PDFProcessor:
    def __init__(self):
        self.input_folder = Path(INPUT_FOLDER)
        self.output_folder = Path(OUTPUT_FOLDER)
        self.displacement_x = DISPLACEMENT_X_MM * 2.834645  # mm a puntos
        self.displacement_y = DISPLACEMENT_Y_MM * 2.834645  # mm a puntos

    def setup_directories(self):
        """Crear directorios necesarios"""
        self.output_folder.mkdir(exist_ok=True)

    def find_pdf_files(self):
        """Encontrar archivos PDF"""
        if not self.input_folder.exists():
            print(f"Error: La carpeta {self.input_folder} no existe")
            return []
        return list(self.input_folder.glob("*.pdf"))

    def process_pdf(self, input_path):
        """Procesar un archivo PDF"""
        try:
            # Abrir PDF
            doc = fitz.open(input_path)

            # Procesar cada página
            for page_num in range(len(doc)):
                page = doc[page_num]

                # Crear una matriz de transformación
                matrix = fitz.Matrix(
                    1, 0, 0, 1, self.displacement_x, self.displacement_y)

                # Aplicar transformación usando el método correcto
                # Envolver el contenido existente con comandos de transformación
                content_stream = f"q\n{matrix.a} {matrix.b} {matrix.c} {matrix.d} {matrix.e} {matrix.f} cm\n"

                # Insertar al inicio usando fitz.TOOLS
                success = fitz.TOOLS._insert_contents(
                    page, content_stream.encode(), False)

                # Insertar comando de restauración al final
                fitz.TOOLS._insert_contents(page, b"\nQ", True)

            # Guardar
            output_path = self.output_folder / input_path.name
            doc.save(output_path)
            doc.close()

            return True

        except Exception as e:
            print(f"Error procesando {input_path.name}: {e}")
            return False

    def run(self):
        """Ejecutar procesamiento"""
        print("PDF CONTENT SHIFTER")
        print("=" * 40)

        # Mostrar desplazamiento configurado
        if DISPLACEMENT_X_MM != 0 and DISPLACEMENT_Y_MM != 0:
            print(
                f"Desplazamiento: X={DISPLACEMENT_X_MM}mm, Y={DISPLACEMENT_Y_MM}mm")
        elif DISPLACEMENT_X_MM != 0:
            direction = "derecha" if DISPLACEMENT_X_MM > 0 else "izquierda"
            print(
                f"Desplazamiento: {abs(DISPLACEMENT_X_MM)}mm hacia la {direction}")
        elif DISPLACEMENT_Y_MM != 0:
            direction = "arriba" if DISPLACEMENT_Y_MM > 0 else "abajo"
            print(
                f"Desplazamiento: {abs(DISPLACEMENT_Y_MM)}mm hacia {direction}")
        else:
            print("Desplazamiento: Sin movimiento configurado")
        print()

        # Preparar
        self.setup_directories()
        pdf_files = self.find_pdf_files()

        if not pdf_files:
            print("No hay archivos para procesar")
            return

        print(f"Directorio de salida: {self.output_folder}")
        print(f"Encontrados {len(pdf_files)} archivos PDF")
        print()

        # Procesar archivos
        successful = 0
        for pdf_file in pdf_files:
            print(f"Procesando: {pdf_file.name}")
            if self.process_pdf(pdf_file):
                successful += 1
                print(f"Completado: {pdf_file.name}")

        # Resumen
        print()
        print(f"Procesados: {successful}/{len(pdf_files)}")
        if successful == len(pdf_files):
            print("Completado exitosamente!")


def main():
    try:
        processor = PDFProcessor()
        processor.run()
    except KeyboardInterrupt:
        print("\nCancelado")
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
