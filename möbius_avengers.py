from matplotlib.tri import Triangulation
import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection="3d")

t = np.linspace(0,2*np.pi, 40)
w = 0.3
s = np.linspace(-w, w, 10)
T,S = np.meshgrid(t, s)

tri = Triangulation(np.ravel(S), np.ravel(T))

R = 1
x = np.ravel((R+S*np.cos(T/2))*np.cos(T))
y = np.ravel((R+S*np.cos(T/2))*np.sin(T))
z = np.ravel((S*np.sin(T/2)))
ax.plot_trisurf(x,y,z,triangles=tri.triangles)

plt.show()
