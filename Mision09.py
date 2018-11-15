# Autor: Luisa Fernanda Arellano Alvarado
# Misión 09


def extraerPares(lista):
        nuevaLista = []
        for dato in lista:
            if dato % 2 == 0:
               nuevaLista.append(dato)
        return nuevaLista


def extraerMayoresPrevio(lista):
    nueva = []
    for k in range(1, len(lista)):
        if lista[k] > lista[k - 1]:
            nueva.append(lista[k])
    return nueva


def intercambiarParejas(lista):
    listaimpar = lista[1::2]
    listaPar = lista[0::2]
    Nueva =[]
    for n in range(len(lista)//2):
        Nueva.append(listaimpar[n])
        Nueva.append(listaPar[n])
        if len(lista)%2 == 1:
            Nueva.append(lista[len(lista)-1])
    return Nueva


def intercambiarMM(lista):
        if lista == []:
            return lista
        minimo = min(lista)
        maximo = max(lista)
        Max = lista.index(maximo)
        Min = lista.index(minimo)
        lista.remove(lista[Max])
        lista.remove(lista[Min])
        lista.insert(Min, maximo)
        lista.insert(Max, minimo)
        return lista


def promediarCentro(lista):
    if len(lista) <= 2:
        return 0
    else:
        nueva = lista.copy()
        nueva.remove(min(nueva))
        nueva.remove(max(nueva))
        promedio = sum(nueva) // len(nueva)
    return promedio


def calcularEstadistica(lista):
    suma = sum(lista)
    Lista = len(lista)
    if Lista == 0:

        return 0, 0
    else:
        m = suma / Lista
        contador = 0
        for valor in lista:
            distancia = (valor - m)**2
            contador = contador + distancia
            desviacion = (contador / (lista-1)) ** (1 / 2)
        return m, desviacion


def main():
    print('---------------------------------------------')
    print('Ejercicio 1:')
    for x in [[1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55], [5, 7, 3], []]:
        print('La lista', x, 'regresa ', extraerPares(x))
    print('--------------------------------------------------------')
    print('Ejercicio 2:')

    for x in [[1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55], [5, 4 , 3 , 2], []]:
        print('Lista original', x, ', regresa', extraerMayoresPrevio(x))
    print('---------------------------------------------------')
    print('Ejercicio 3:')
    for x in [[1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55], [1, 2 , 3], [3], []]:
        print('La lista', x, 'regresa', intercambiarParejas(x))
    print('---------------------------------------------------')
    print('Ejercicio 4: ')
    for x in [[5, 9 , 3, 22, 19, 31, 10, 7], [1, 2 , 3], []]:
        print('La lista', x, 'regresa', intercambiarMM(x))
    print('-----------------------------------------------------')




    print('Ejercicio 5:')
    for x in [[70, 80, 90], [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85], [20, 55, 30, 5, 55, 5], [5, 9, 1, 8], []]:
        print('La lista',x, 'regresa ', promediarCentro(x))



main()














