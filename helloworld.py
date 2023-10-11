m = float(input("Ingrese el valor de m: "))
b = float(input("Ingrese el valor de b: "))
# Definir la función lineal y = mx + b
def funcion_lineal(m, b):
    return -b / m

import matplotlib.pyplot as plt 
import numpy as np

plt.style.use('seaborn-v0_8-notebook')

%matplotlib notebook
x = np.linspace(0,5,10)
m = float(input("Ingrese el valor de m: "))
b = float(input("Ingrese el valor de b: "))
# Definir la función lineal y = mx + b
def f(x):
    return m*x+b
plt.plot(x,f(x))


senooo 
import math
import numpy as np
import matplotlib.pyplot as plt

x = np.array(range(500))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = math.sin(x[i])

#el gráfico
plt.ion()
plt.plot(x,y)
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
print(f'La raíz de la función lineal es x = {funcion_lineal(m, b)}')
print("Hello world")
print("explode the world")
