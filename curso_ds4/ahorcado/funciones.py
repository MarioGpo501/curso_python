""" funciones auxiliares para el juego del ahorcado """

import string
import unicodedata
from random import choice

def carga_archivo_texto(archivo:str)->list:
    ''' Carga un archivo de texto y regresa una lista con las oraciones
    del archivo '''
    with open(archivo,  'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantillas(nombre_plantilla:str)->dict:
    """ carga las plantillas del juego apartir de un archivo de texto """
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
    """ despliega la plantilla del nivel seleccionado """
    if nivel in diccionario:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)
    return diccionario[nivel]

def obten_palabras(lista:list)->list:
    """ obtiene las palabras de un texto """
    texto = ' '.join(lista[120:])
    palabras = texto.split()
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    # removemos signos de puntuacion y caracteres especiales
    set_palabras = {palabra.strip(string.punctuation) for palabra in set_palabras}
    # removemos numeros, parentesis y corchetes
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}
    # removemos acentos
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ASCII', 'ignore').decode('ascii') for palabra in set_palabras}

    return list(set_palabras)

def adivina_letra(abc:dict, palabra:str, letras_adivinadas:str, turnos: int):
    """ adivina una letra de la palabra """
    palabra_oculta = ''

    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += '_'
    print(f'Tienes {turnos} aportunidades de fallar')
    print(f'El abecedario es: {abc}')
    print(f'La palabra es: {palabra_oculta}')
    letra = input('Ingresa una letra: ')
    letra = letra.lower()
    if letra in abc:
        if abc[letra] == "*":
            print('Letra ya adivinada')
        else:
            abc[letra] = "*"
            if letra in palabra:
                letras_adivinadas.add(letra)
                print('Letra correcta')
            else:
                print('Letra incorrecta')
                turnos -= 1

if __name__ == '__main__':
    plantillas = carga_plantillas('plantilla')
    despliega_plantilla(plantillas, 5)
    lista_oraciones = carga_archivo_texto('./datos/pg15532.txt')

    lista_palabras = obten_palabras(lista_oraciones)
    print(len(lista_palabras))
    p = choice(lista_palabras)
    print(p)

    abcdario = {letra: letra for letra in string.ascii_lowercase}
    adivinadas = set()
    t = 5 # oportunidades
    adivina_letra(abcdario, p, adivinadas, t)
    adivina_letra(abcdario, p, adivinadas, t)