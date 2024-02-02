from scipy.integrate import solve_ivp
import numpy as np


T_ambiente = float(input("Ingrese la temperatura ambiente: "))
T_inicial = float(input("Ingrese la temperatura inicial del pastel: "))
T_30min = float(input("Ingrese la temperatura del pastel después de 30 minutos: "))
T_objetivo = float(input("Ingrese la temperatura objetivo del pastel: "))
tiempo_30min = 30


k = -1 / tiempo_30min * np.log((T_ambiente - T_inicial) / (T_ambiente - T_30min))

# Definir la ecuación diferencial

def dT_dt(t, T):
    return k * (T - T_ambiente)

# Resolver la ecuación diferencial
sol = solve_ivp(dT_dt, [0, 100], [T_inicial], dense_output=True)

# Encontrar el tiempo necesario para que la temperatura sea de 100 F
t_objetivo = sol.t[sol.y[0] <= T_objetivo][0]

print(f"El pastel estará apróximadamente a {T_objetivo} F después de {t_objetivo} minutos.")
