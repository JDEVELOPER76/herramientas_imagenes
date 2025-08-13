Documentación de Imagen_Tools
Descripción general
Imagen_Tools es una clase que ofrece varias utilidades para trabajar con imágenes usando la librería Pillow en Python. Permite transformar formatos, redimensionar imágenes, agregar marcas de agua, mostrar metadatos, convertir a iconos .ICO y procesar imágenes en carpetas.

Cada método incluye validaciones y manejo de errores para evitar que el programa se interrumpa por entradas incorrectas o problemas en archivos.

Métodos
transformar_IMG_ext(origen, destino, extension)
Convierte una imagen ubicada en origen a un nuevo formato dado por extension y la guarda con el nombre base destino.

Parámetros:

origen (str): Ruta del archivo original.

destino (str): Ruta base (sin extensión) donde se guardará la imagen convertida.

extension (str): Extensión/ formato destino (por ejemplo, "jpg", "png").

Validaciones:

Verifica que el archivo de origen exista.

Valida que la extensión sea una cadena válida.

Maneja transparencia para formatos que no la soportan (JPEG).

configurarIMG_enCarpetas(carpeta_origen, carpeta_destino, extension_salida, ancho=None, alto=None)
Convierte y opcionalmente redimensiona todas las imágenes dentro de carpeta_origen, guardándolas en carpeta_destino con el formato extension_salida.

Parámetros:

carpeta_origen (str): Ruta del directorio origen.

carpeta_destino (str): Ruta del directorio destino.

extension_salida (str): Extensión/formato para las imágenes resultantes.

ancho (int, opcional): Nuevo ancho para redimensionar. Si es None, mantiene el ancho original.

alto (int, opcional): Nuevo alto para redimensionar. Si es None, mantiene el alto original.

Validaciones:

Verifica que las carpetas existan o crea la carpeta destino.

Valida extensiones y dimensiones positivas.

Maneja formatos y transparencia correctamente.

redimensionar_img(img_origen, img_destino, ancho, alto)
Redimensiona una imagen individual y la guarda en la ruta destino.

Parámetros:

img_origen (str): Ruta del archivo de imagen original.

img_destino (str): Ruta donde se guardará la imagen redimensionada.

ancho (int): Ancho deseado en píxeles.

alto (int): Alto deseado en píxeles.

Validaciones:

Verifica que la imagen exista.

Valida que ancho y alto sean enteros positivos.

convertir_aICO(imagen, resultado)
Convierte una imagen a formato icono .ICO con tamaño 256x256 px.

Parámetros:

imagen (str): Ruta de la imagen original.

resultado (str): Ruta base (sin extensión) donde se guardará el .ICO.

Validaciones:

Verifica que la imagen exista.

mostrar_metaDATOS(imagen)
Muestra en consola información básica y metadatos EXIF de una imagen.

Parámetros:

imagen (str): Ruta de la imagen.

Validaciones:

Verifica que la imagen exista.

agregar_marca_agua(imagen, salida, texto="Tu marca de agua", posicion=(10, 10), tamaño_fuente=20)
Agrega una marca de agua con texto semitransparente en la posición indicada de la imagen y la guarda.

Parámetros:

imagen (str): Ruta de la imagen original.

salida (str): Ruta donde se guardará la imagen con marca de agua.

texto (str): Texto para la marca de agua.

posicion (tuple): Coordenadas (x, y) donde se colocará el texto.

tamaño_fuente (int): Tamaño de la fuente del texto.

Validaciones:

Verifica que la imagen exista.

Valida tipos y formato de texto, posición y tamaño.

SOPORTE_IMG (propiedad)
Devuelve una cadena con los formatos de imagen soportados por Pillow.

Dependencias
Pillow (pip install pillow)

EQUIVALENCIAS_FORMATOS en plugins_tools: Diccionario para mapear extensiones a formatos compatibles con Pillow.