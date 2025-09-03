import fitz
import os


def normalize_orientation(input_path, output_path, target_orientation="vertical"):
    """
    Normaliza la orientación de las páginas de un archivo PDF.

    :param input_path: Ruta del archivo PDF de entrada.
    :param output_path: Ruta del archivo PDF de salida.
    :param target_orientation: Orientación objetivo, "vertical" o "horizontal".
    """
    if target_orientation not in ["vertical", "horizontal"]:
        raise ValueError(
            "La orientación objetivo debe ser 'vertical' o 'horizontal'.")

    doc = fitz.open(input_path)

    for page in doc:
        # Obtener el tamaño de la página
        width, height = page.rect.width, page.rect.height

        if target_orientation == "vertical" and width > height:
            # Rotar 90 grados para hacerla vertical
            page.set_rotation((page.rotation + 90) % 360)
        elif target_orientation == "horizontal" and height > width:
            # Rotar 90 grados para hacerla horizontal
            page.set_rotation((page.rotation + 90) % 360)

    # Guardar el archivo con las páginas rotadas
    doc.save(output_path)
    doc.close()


if __name__ == "__main__":
    # Directorio de entrada y salida
    input_dir = "ToMove"
    output_dir = "Processed"

    # Crear el directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)

    # Iterar sobre los archivos en el directorio de entrada
    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)

        if filename.endswith(".pdf"):
            output_path = os.path.join(output_dir, filename)

            print(f"Normalizando orientación de: {filename}")
            normalize_orientation(input_path, output_path,
                                  target_orientation="vertical")
        else:
            print(f"Eliminando archivo no válido: {filename}")
            os.remove(input_path)

    print("Proceso completado.")
