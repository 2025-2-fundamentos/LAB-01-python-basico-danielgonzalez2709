"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open('files/input/data.csv', 'r') as file:
        conteo = {}
        for line in file:
            line = line.strip()
            if line:
                columns = line.split('\t')
                letra = columns[0]
                conteo[letra] = conteo.get(letra, 0) + 1

        resultado = sorted(conteo.items())
        return resultado
