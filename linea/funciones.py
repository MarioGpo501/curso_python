""""
Funciones auxiliares para el programa linea
"""
import matplotlib.pyplot as plt

def calcular_y(x,m,b):
    '''
    Calcula y de acuerdo a la pendiente m y el punto de interseccion en y b 
    Retorna el valor de y 
    '''
    return m*x+b


def grafica_linea(X:list, Y:list, m:float, b:float):

    plt.plot(X,Y)
    plt.title(f'Linea recta con pendiente={m} e interseccion en y={b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()




if __name__ == "__main__":
    x = 0 
    m = 3
    b = 2
    y = calcular_y(x,m,b)
    if y == 2:
        print("Prueba exitosa")
    else: 
        print("Prueba fallida")