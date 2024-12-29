import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create data with a custom grid size
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z3 = np.sin(X) * np.cos(Y)

# Create wireframe plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z3, color='red')

# Titles and labels
ax.set_title('3D Wireframe Plot with Custom Grid Size')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.savefig('custom_grid_wireframe.png')  # Save the figure
plt.show()
