def is_year_leap(year):
    """
    Función que determina si un año es bisiesto.

    Parámetros:
    year (int): Año a verificar

    Devuelve:
    bool: True si el año es bisiesto, False en caso contrario
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Datos de prueba
test_data = [1976, 2000, 2016, 1987, 2025]
test_results = [False, True, True, False,True, False]

# Pruebas
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
is_year_leap(1976)
print(result)
