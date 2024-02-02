import math

def calcular_poblacion_inicial(poblacion_despues_de_3_anios, t=3):
    # Usando la fórmula c = P / e^(kt) para encontrar la población inicial
    c = poblacion_despues_de_3_anios / math.exp(t * k)
    return c

def calcular_poblacion_en_tiempos_futuros(c, t):
    # Usando la fórmula P = ce^(kt) para encontrar la población en tiempos futuros
    poblacion_futura = c * math.exp(t * k)
    return poblacion_futura

poblacion_despues_de_3_anios = 10000
t = 10

k = 0.05

# Calcular la población inicial
poblacion_inicial = calcular_poblacion_inicial(poblacion_despues_de_3_anios)

# Calcular la población en 10 años
poblacion_en_10_anios = calcular_poblacion_en_tiempos_futuros(poblacion_inicial, t)

# Mostrar resultados
print(f'Población inicial: {poblacion_inicial:.2f}')
print(f'Población en 10 años: {poblacion_en_10_anios:.2f}')
