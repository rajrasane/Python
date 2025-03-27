import numpy as np

n = int(input("Enter how many data points you want : "))

x = np.zeros(n)
y = np.zeros(n)

print("Enter data point values : ")

for i in range(n):
    x[i] = float(input(f"x[{i}] = "))
    y[i] = float(input(f"y[{i}] = "))

xp = float(input("Enter point to interpolate : "))

yp = 0

for i in range(n):
    p = 1
    for j in range(n):
        if i!=j:
            p *= (xp-x[j])/(x[i]-x[j])
    yp += p * y[i]

print(f"Interpolated Value for {xp} is {yp}")