import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection="3d")

z = np.linspace(0,1,100)
x = z*np.sin(25*z)
y = z*np.cos(25*z)

ax.plot3D(x,y,z,'green')
ax.set_title("3D Plot")

plt.show()