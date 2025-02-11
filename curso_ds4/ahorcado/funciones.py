""" funciones auxiliares para el juego del ahorcado """

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

if __name__ == '__main__':
    plantillas = carga_plantillas('plantilla')
    despliega_plantilla(plantillas, 5)
    despliega_plantilla(plantillas, 4)
    despliega_plantilla(plantillas, 3)
    despliega_plantilla(plantillas, 2)
    despliega_plantilla(plantillas, 1)
    despliega_plantilla(plantillas, 0)
    despliega_plantilla(plantillas, 6)