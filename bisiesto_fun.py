def es_ano_bisiesto(ano):
    """
    Función que determina si un año es bisiesto.

    Parámetros:
    ano (int): Año a verificar

    Devuelve:
    bool: True si el año es bisiesto, False en caso contrario
    """
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Pruebas
años_prueba = [1600, 1700, 1800, 1900, 2000, 2004, 2018, 2020, 2023, 2025]
resultados = {año: es_ano_bisiesto(año) for año in años_prueba}

es_ano_bisiesto(2025)
print(resultados)
