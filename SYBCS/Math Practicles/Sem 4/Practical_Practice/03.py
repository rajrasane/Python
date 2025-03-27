import numpy as np

print("Enter how many data points : ")
n = int(input("n = "))

x = np.zeros(n)
y = np.zeros(n)

print("Enter values = ")

for i in range(0,n):
    x[i] = float(input(f"x[{i}] = "))
    y[i] = float(input(f"y[{i}] = "))

xp = float(input("Enter the point to interpolate : "))

yp = 0

for i in range(n):
    p = 1
    for j in range(n):
        if i!=j:
            p *= (xp-x[j]) / (x[i]-x[j])
    yp += p * y[i]

print(f"Interpolated Value at f{xp} = {yp:.4f}")