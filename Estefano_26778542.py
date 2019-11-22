#!/usr/bin/env python3
"""
Proyecto Polinomio de Lagrange.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

def polinomio_lagrange(X, Y):
    """
    Implementa y retorna el Polinomio de Lagrange para las listas X e Y.

    Parámetros:
    X: lista de valores de la variable independiente.
    Y: lista de valores de la variable dependiente.
    """

    if len(X) != len(Y): raise ValueError("Dimensiones diferentes en X e Y.")

    # Ordena el par (x, y) en forma ascendente por x.
    pares = list(zip(X, Y))
    pares.sort(key = lambda x: x[0])
    X, Y  = zip(*pares)

    def L(x,k):
        _ = 1
        for i in range(len(X)):
            if i != k:
                aux = (x - X[i])/(X[k]-X[i])
                _ *= aux
        return _
    def polinomio(x):
        _ = 0
        i=0
        for y in Y:
            aux = y*L(x,i)          
            _+=aux
            i+=1
        return _

    return polinomio


if __name__ == '__main__':
    # Pruebe aquí su Polinomio de Lagrange ...

    X=[0,1]
    Y=[0.5,0.8776]
    p=polinomio_lagrange(X,Y)

    print("x:", end=" ")
    for numero in X:
        print (numero, end=" ")
    print("")
    print("y:", end=" ")
    for numero in Y:
        print (numero, end=" ")
    print("")       
    print("P(0):",p(1))
