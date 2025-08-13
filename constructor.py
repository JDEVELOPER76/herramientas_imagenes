from ImagenTools import Imagen_Tools as img
import pyfiglet
from plugins_tools import ayuda , mas
import os

name = pyfiglet.figlet_format("IMG TOOLS")

def menu():
    print(name)
    print("")
    print("usa /ayuda para obtener informacion sobre los comandos")
    print("usa /mas para saber mas sobre la aplicacion")
    print("usa /casa para limpiar la consola")
    print("usa /salir para salir ")


def constructor():
    try:
        menu()
        home = True
        while home:
            usuario = input()
            if usuario == "":
                menu() == False
            elif usuario == "/casa":
                os.system("cls")
                menu() == True
            elif usuario == "/ayuda":
                print(ayuda["comando_ayuda"])
            elif usuario == "/mas":
                print("")
                print(mas["comando_mas"])
            elif usuario == "/agregar_marca_agua":
                nombre_img = input("Nombre de la imagen con el .png u otro :")
                nombre_salida = input("Nombre de imagen (resultado).png u otro ")
                marca_agua = input("Ingresa la marca de agua :")
                posicion_marca = tuple(map(int, input("Posicion x - y de marca de agua ejemplo ->(20,20) :").split(',')))
                tamaño_letra = input("Ingresa el tamo de la letra :")
                img.agregar_marca_agua(nombre_img , nombre_salida , marca_agua , posicion_marca , tamaño_letra)
            elif usuario == "/convertir_aICO":
                nombre_img_to_ico = input("Nombre de la imagen con la extension (.png) :")
                icono_resultado = input("Nombre del resultado sin extension :")
                img.convertir_aICO(nombre_img_to_ico , icono_resultado)
            elif usuario == "/mostrar_metaDATOS":
                img_metadatos = input("Ingrese el nombre de la imagen con extension (.png) :")
                img.mostrar_metaDATOS(img_metadatos)
            elif usuario == "/redimensionar_img":
                img_aMODIFICAR = input("Ingresa el nombre de la imgen con la extension (.png) :")
                img_Modificada = input("Ingresa el nombre que desas poner el nombre de la imagen con la extension (.png) :")
                ancho_img = int(input("Ingresa el ancho de la imagen :"))
                alto_img = int(input("Ingresa el alto de la imagen :"))
                img.redimensionar_img(img_aMODIFICAR , img_Modificada , ancho_img , alto_img)
            elif usuario == "/configurarIMG_enCarpetas":
                carpeta_origen = input("Ingresa la ruta de la carpeta de origen :")
                carpeta_destino = input("Ingresa la ruta de la carpeta de destino :")
                extension_salida = input("Ingresa la extension de salida :")
                ancho = int(input("Ingresa el ancho de la imagen (opcional) :"))
                alto = int(input("Ingresa el alto de la imagen (opcional) :"))
                img.configurarIMG_enCarpetas(carpeta_origen , carpeta_destino , extension_salida , ancho , alto)
            elif usuario == "/transformar_IMG_ext":
                img_inicio = input("Ingresa la ruta de la imagen de inicio con la extension :")
                img_destino = input("Ingresa la ruta de la imagen sin la extension :")
                extension_salida = input("Ingresa la extension de salida :")
                img.transformar_IMG_ext(img_inicio , img_destino , extension_salida)
            elif usuario == "/SOPORTE_IMG":
                print(img.SOPORTE_IMG)
            elif usuario == "/salir":
                print("EJECUCION FINALIZADA")
                home = False
            else:
                print(f"Usa /ayuda y ver los comandos [{usuario}] no disponible")
    except:
        print("Error al ejecutar")

constructor()











