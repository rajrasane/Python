from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + np.abs(y) ** 3))

theta = 2 * np.pi * np.random.random(100)
r = 6 * np.random.random(100)

x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))
z = f(x, y)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5)

ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='green')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.title('3D Surface Triangulation with Scatter Plot')

plt.show()
