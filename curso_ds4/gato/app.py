""" 
Este archivo es el punto de entrada a la 
aplicacion. Aquí se importan las funciones de tablero.py y se ejecutan 
en un ciclo while

 """

import tablero

def main(): 
    """ Funcion principal """
    X = {'G':0,'P':0,'E':0}
    O = {'G':0,'P':0,'E':0}
    score = {'X':X,'O':O}

    numeros = [str(i) for i in range(1,10)]
    corriendo = True
    while corriendo is True:
        dsimbolos = {x:x for x in numeros}
        g = tablero.juego(dsimbolos)
        tablero.actualizar_score(score,g)
        tablero.despliega_tablero(score)
        seguir = input('Quieres seguir (s/n): ')
        if seguir.lower() == 'n':
            corriendo= False

if __name__ == '__main__':
    main()