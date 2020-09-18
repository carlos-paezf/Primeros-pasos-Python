import numpy as np
import matplotlib.pyplot as plt


# Datos
t = np.linspace(0, 10, 1000)


# Trayectoria
def s(t):
    return np.array([np.sin(t), np.cos(t), np.exp(t)])


# Recoleccion de los datos
x, y, z = s(t)


# Grafica
fig = plt.figure('Trayectoria')
ax = fig.gca(projection='3d')

ax.plot(x, y, z, 'r.')

plt.show()
