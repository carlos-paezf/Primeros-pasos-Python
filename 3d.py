import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation


#datos
'''
x = np.linspace(0,4,101)
y = x**2
'''

t = np.linspace(0,10,51)
x = np.linspace(-np.pi, np.pi, 11)
y = np.linspace(-np.pi, np.pi, 11)


xmesh, ymesh = np.meshgrid(x,y)


def f(x,y,t):
	return np.sin(y+t)*np.cos(x)



#grafica
fig = plt.figure()
ax = fig.gca(projection='3d')


#actualizar
def actualizar(i):
	ax.clear()
	'''
	ax.plot(x[:i],y[:i])
	plt.title(str(x[i]))
	plt.xlim(min(x), max(x))
	plt.ylim(min(y), max(y))
	'''
	zmesh = f(xmesh, ymesh, t[i])
	ax.plot_surface(xmesh, ymesh, zmesh)
	plt.title(str(t[i]))


#animation
ani = animation.FuncAnimation(
	fig, 
	actualizar, 
# 	range(len(x)),
	range(len(t)),
	interval=1, 
	repeat=True
	)


plt.show()