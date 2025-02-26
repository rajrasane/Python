# using the subplot function

import matplotlib.pyplot as plt
import numpy as np

# plot no 1
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array([30,33,34,34,35,31,30,28,31,33,33,31])

plt.subplot(1,2,1)
plt.bar(x,y)
plt.xlabel("Months in Year")
plt.ylabel("highest temperature in that month")

plt.title("Highest Temp Record  ")
# plt.show()

# plot 2
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array([20,23,24,19,20,19,20,18,17,18,13,14])

plt.subplot(1,2,2)
plt.bar(x,y)
plt.xlabel("Months in Year")
plt.ylabel("lowest temperature in that month")

plt.title("Lowest Temp Record")
plt.suptitle("Temperature and month record")
plt.show()
