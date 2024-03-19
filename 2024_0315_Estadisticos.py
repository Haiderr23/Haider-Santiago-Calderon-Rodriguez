#Haider Santiago Calderón Rodríguez 20211005075
from math import sqrt

v = [45, 50, 30, 40, 35]

def promedio(v):
    k = len(v)
    x = 0
    for i in range(k):
        x += v[i]
    prom = x / k
    return prom

print("Promedio:",promedio(v))

def desv_est(v):
    k = len(v)
    prom = promedio(v)
    x = 0
    for i in range(k):
        x += (v[i] - prom)**2
    desv_est = sqrt(x / k)
    return desv_est

print("Desviacion estandar:",desv_est(v))

def varianza(v):
    k = len(v)
    prom = promedio(v)
    x = 0
    for i in range(k):
        x += (v[i] - prom)**2
    vari = (x / k)
    return vari

print("Varianza:",varianza(v))
