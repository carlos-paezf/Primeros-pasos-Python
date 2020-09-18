import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def z(x, y):
    return np.sin(np.sqrt(x**2 + y**2))


fig = plt.figure()
ax = Axes3D(fig)

x = np.linspace(-4, 4, 50)
y = np.linspace(-4, 4, 50)
X, Y = np.meshgrid(x, y)

'''
ax.plot_surface(X, Y, z(X, Y))      # Grafica de Superficie
ax.contour(X, Y, z(X, Y))           # Grafica de Contorno
'''
ax.contourf(X, Y, z(X, Y))          # Grafica de Contorno Rellena
plt.show()
