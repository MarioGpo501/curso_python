""" 
    Programa  principal del juego del ahorcado
"""
import string 
import unicodedata
from random import choice
import funciones as fn

def main(archivo_texto:str, nombre_plantilla="plantilla"):
   """ Programa principal del juego del ahorcado 
   """

    # cargamos las plantillas
    
    plantillas = fn.carga_plantillas(nombre_plantilla)
    oraciones = fn.carga_archivo_texto(archivo_texto)
    #obtenemos las palabras del archivo de texto
    palabras = fn.obten_palabras(oraciones)
    o = 5 # oportunidades a fallar 
    p = choice(palabras) # palabra a adivinar
    abcdarios = {letra:letra for letra in string.ascci_lowercase}
    adivinadas = set()    
    while o > 0:
        fn.despliega_plantilla(plantillas, o)
        fn.adivina_letra(abcdarios,p,adivinadas,o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Felicidades, adivinaste la palabra')
            break

if __name__ == '__main__':
    archivo = './datos/pg15532.txt'
    main(archivo)

