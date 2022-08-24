import numpy as np

def filter(array, *args):
    
    filtros = args[0]

    for filtro in args:
        filtros = np.logical_and(filtros, filtro)
    array = array[filtros]
    
    return array


def filterIndex(*args):
    
    filtros = args[0]
    indices = []
    for filtro in args:
        filtros = np.logical_and(filtros, filtro)
    indices = np.where(filtros)
    
    return indices[0]