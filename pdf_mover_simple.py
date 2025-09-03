#!/usr/bin/env python3
"""
PDF Content Shifter - Simple Version
===================================

Script corregido para mover contenido de PDFs.
Utiliza el método show_pdf_page para mantener calidad vectorial.
"""

import sys
import fitz
from pathlib import Path
from config import DISPLACEMENT_X_MM, DISPLACEMENT_Y_MM, INPUT_FOLDER, OUTPUT_FOLDER


class PDFProcessor:
    def __init__(self):
        self.input_folder = Path(INPUT_FOLDER)
        self.output_folder = Path(OUTPUT_FOLDER)
        # Convertir mm a puntos PDF (1 mm = 2.834645 puntos)
        self.displacement_x = DISPLACEMENT_X_MM * 2.834645
        self.displacement_y = DISPLACEMENT_Y_MM * 2.834645

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
        """Procesar un archivo PDF usando show_pdf_page"""
        try:
            # Abrir PDF original
            source_doc = fitz.open(input_path)

            # Crear documento de destino
            dest_doc = fitz.open()

            # Procesar cada página
            for page_num in range(len(source_doc)):
                source_page = source_doc[page_num]
                page_rect = source_page.rect

                # Crear nueva página
                dest_page = dest_doc.new_page(
                    width=page_rect.width, height=page_rect.height)

                # Calcular rectángulo de destino con desplazamiento
                dest_rect = fitz.Rect(
                    self.displacement_x,
                    self.displacement_y,
                    page_rect.width + self.displacement_x,
                    page_rect.height + self.displacement_y
                )

                # Mostrar la página original en la nueva posición
                # show_pdf_page mantiene la calidad vectorial
                dest_page.show_pdf_page(
                    dest_rect,     # rectángulo destino
                    source_doc,    # documento fuente
                    page_num,      # página fuente
                    clip=None,     # sin recorte
                    rotate=0,      # sin rotación
                    oc=0,          # sin contenido opcional
                    overlay=True,  # en primer plano
                    keep_proportion=True  # mantener proporción
                )

            # Cerrar documento fuente
            source_doc.close()

            # Guardar documento procesado
            output_path = self.output_folder / input_path.name
            dest_doc.save(output_path, garbage=3, deflate=True)
            dest_doc.close()

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
