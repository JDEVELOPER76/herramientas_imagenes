from PIL import Image
from PIL import ImageDraw, ImageFont
import os
from plugins_tools import EQUIVALENCIAS_FORMATOS

class Imagen_Tools:
    def __init__(self):
        pass

    @staticmethod
    def transformar_IMG_ext(origen, destino, extension):
        if not os.path.isfile(origen):
            print(f"Error: El archivo origen '{origen}' no existe.")
            return
        if not extension or not isinstance(extension, str):
            print(f"Error: La extensión '{extension}' no es válida.")
            return
        try:
            imagen = Image.open(origen)
            formato = EQUIVALENCIAS_FORMATOS.get(extension.lower(), extension.upper())

            if formato in ["JPEG", "JPG"]:
                if imagen.mode in ("RGBA", "LA") or (imagen.mode == "P" and "transparency" in imagen.info):
                    imagen = imagen.convert("RGB")

            ruta_salida = f"{destino}.{extension.lower()}"
            imagen.save(ruta_salida, format=formato)
            print(f"{origen} guardada como {ruta_salida}")
        except Exception as e:
            print(f"Error al convertir {origen}: {e}")

    @staticmethod
    def configurarIMG_enCarpetas(carpeta_origen, carpeta_destino, extension_salida, ancho=None, alto=None):
        if not os.path.exists(carpeta_origen) or not os.path.isdir(carpeta_origen):
            print(f"Error: La carpeta origen '{carpeta_origen}' no existe o no es un directorio.")
            return
        if not extension_salida or not isinstance(extension_salida, str):
            print(f"Error: La extensión de salida '{extension_salida}' no es válida.")
            return
        if ancho is not None and (not isinstance(ancho, int) or ancho <= 0):
            print(f"Error: El ancho '{ancho}' debe ser un entero positivo.")
            return
        if alto is not None and (not isinstance(alto, int) or alto <= 0):
            print(f"Error: El alto '{alto}' debe ser un entero positivo.")
            return

        if not os.path.exists(carpeta_destino):
            try:
                os.makedirs(carpeta_destino)
            except Exception as e:
                print(f"Error al crear carpeta destino '{carpeta_destino}': {e}")
                return

        extensiones_soportadas = [ext.lower() for ext in Image.registered_extensions().keys()]
        formato = EQUIVALENCIAS_FORMATOS.get(extension_salida.lower(), extension_salida.upper())

        for archivo in os.listdir(carpeta_origen):
            if any(archivo.lower().endswith(ext) for ext in extensiones_soportadas):
                ruta_origen = os.path.join(carpeta_origen, archivo)
                try:
                    imagen = Image.open(ruta_origen)
                    
                    if formato == "JPEG":
                        if imagen.mode in ("RGBA", "LA") or (imagen.mode == "P" and "transparency" in imagen.info):
                            imagen = imagen.convert("RGB")

                    if ancho is not None and alto is not None:
                        imagen = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)

                    nombre_sin_ext = os.path.splitext(archivo)[0]
                    ruta_destino = os.path.join(carpeta_destino, f"{nombre_sin_ext}.{extension_salida.lower()}")

                    imagen.save(ruta_destino, format=formato)
                    print(f"{archivo} guardada como {extension_salida.upper()}.")
                except Exception as e:
                    print(f"Error procesando {archivo}: {e}")

    @staticmethod
    def redimensionar_img(img_origen, img_destino, ancho, alto):
        if not os.path.isfile(img_origen):
            print(f"Error: La imagen origen '{img_origen}' no existe.")
            return
        if not isinstance(ancho, int) or ancho <= 0:
            print(f"Error: El ancho '{ancho}' debe ser un entero positivo.")
            return
        if not isinstance(alto, int) or alto <= 0:
            print(f"Error: El alto '{alto}' debe ser un entero positivo.")
            return

        try:
            imagen = Image.open(img_origen)
            imagen_tratada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)
            imagen_tratada.save(img_destino)
            print(f"Éxito: {img_destino}")
        except Exception as e:
            print(f"Error al redimensionar imagen: {e}")

    @staticmethod
    def convertir_aICO(imagen, resultado):
        if not os.path.isfile(imagen):
            print(f"Error: La imagen '{imagen}' no existe.")
            return
        try:
            img = Image.open(imagen)
            img = img.convert("RGBA")
            img = img.resize((256, 256))
            ruta_salida = f"{resultado}.ICO"
            img.save(ruta_salida)
            print(f"Éxito: {ruta_salida}")
        except Exception as e:
            print(f"Error al convertir a ICO: {e}")

    @staticmethod
    def mostrar_metaDATOS(imagen):
        from PIL import ExifTags
        if not os.path.isfile(imagen):
            print(f"Error: La imagen '{imagen}' no existe.")
            return
        try:
            img = Image.open(imagen)
            print("=== Información básica ===")
            print(f"Formato: {img.format}")
            print(f"Tamaño en píxeles: {img.size}")
            print(f"Modo de color: {img.mode}")
            if "dpi" in img.info:
                dpi_x, dpi_y = img.info["dpi"]
                print(f"DPI (X, Y): {dpi_x}, {dpi_y}")
            print("\n=== Metadatos EXIF ===")
            exif = img.getexif()
            if not exif:
                print("No hay metadatos EXIF en la Imagen o no pudimos encontrarlos.")
            else:
                for tag, value in exif.items():
                    nombre = ExifTags.TAGS.get(tag, tag)
                    if tag == 296:
                        unidades = {1: "sin unidad", 2: "pulgadas", 3: "centímetros"}
                        value = unidades.get(value, value)

                    print(f"{nombre} ({tag}): {value}")
            print("\nÉxito")
        except Exception as e:
            print(f"Error al mostrar metadatos: {e}")

    @staticmethod
    def agregar_marca_agua(imagen, salida, texto="Tu marca de agua", posicion=(10, 10), tamaño_fuente=20):
        if not os.path.isfile(imagen):
            print(f"Error: La imagen '{imagen}' no existe.")
            return
        if not isinstance(texto, str):
            print(f"Error: El texto debe ser una cadena de caracteres.")
            return
        if (not isinstance(posicion, tuple) or len(posicion) != 2 or
                not all(isinstance(coord, int) for coord in posicion)):
            print(f"Error: La posición debe ser una tupla de dos enteros.")
            return
        if not isinstance(tamaño_fuente, int) or tamaño_fuente <= 0:
            print(f"Error: El tamaño de fuente debe ser un entero positivo.")
            return
        try:
            img = Image.open(imagen).convert("RGBA")
            capa = Image.new("RGBA", img.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(capa)
            try:
                fuente = ImageFont.truetype("arial.ttf", tamaño_fuente)
            except IOError:
                fuente = ImageFont.load_default()
                print("Advertencia: No se pudo cargar 'arial.ttf', se usará fuente por defecto.")
            draw.text(posicion, texto, font=fuente, fill=(255, 255, 255, 128))
            img_final = Image.alpha_composite(img, capa)
            img_final.save(salida)
            print(f"Éxito: {salida}")
        except Exception as e:
            print(f"Error al agregar marca de agua: {e}")

    @property
    def SOPORTE_IMG(self):
        formatos = ['BMP', 'DIB', 'EPS', 'GIF', 'ICO', 'PCX', 'PNG', 'PPM', 'SGI', 'TGA', 'XBM', 'JPEG', 'TIFF', 'WebP', 'JPEG 2000']
        return (f"Tipos {formatos}")
