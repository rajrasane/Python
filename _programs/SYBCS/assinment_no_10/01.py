import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6])
y = np.array([20,30,40,50,60,70 ])

plt.plot(x,y)
plt.grid()
plt.title("Sample Table")
plt.xlabel("X Label")
plt.ylabel("Y Label")

plt.show()