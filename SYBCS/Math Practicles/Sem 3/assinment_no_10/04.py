# Plotting Graph of log function

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(2,10)
y=np.log10(x)

plt.plot(x,y)
plt.show()