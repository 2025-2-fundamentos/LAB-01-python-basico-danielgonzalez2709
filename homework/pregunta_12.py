"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open('files/input/data.csv', 'r') as file:
        suma_por_letra = {}
        for line in file:
            line = line.strip()
            if line:
                columns = line.split('\t')
                letra = columns[0]
                pares = columns[4].split(',')

                suma_valores = 0
                for par in pares:
                    valor = int(par.split(':')[1])
                    suma_valores += valor

                suma_por_letra[letra] = suma_por_letra.get(letra, 0) + suma_valores

        return dict(sorted(suma_por_letra.items()))
