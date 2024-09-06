import math

def taylor_serie_elevado_x(valor_x, orden_n):
    # Inicializamos el resultado de la suma de la serie de Taylor
    aproximacion = 0
    # Iteramos desde 0 hasta el orden_n (orden de la serie)
    for i in range(orden_n + 1):
        aproximacion += (valor_x**i) / math.factorial(i)
    return aproximacion

# Parámetros
valor_aproximar = 2.5  # Valor donde queremos aproximar
for orden in range(1, 8):
    # Cálculo de la aproximación usando la serie de Taylor
    valor_aprox = taylor_serie_elevado_x(valor_aproximar, orden)
    print(f"Aproximación de e^{valor_aproximar} usando la serie de Taylor de orden {orden}: {valor_aprox}")

