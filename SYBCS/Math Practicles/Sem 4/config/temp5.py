x = [1, 2, 3, 4, 5]
y = [[41], [62], [65], [50], [17]]

for i in range(1, 5):
    for j in range(4, i - 1, -1):
        y[j].append(y[j][i - 1] - y[j - 1][i - 1])

u = (3.5 - x[-1]) / (x[1] - x[0])  
p = y[-1][0]  
fact = 1
term = 1

for i in range(1, 5):
    term *= (u + (i - 1))
    fact *= i
    p += (term / fact) * y[4][i]  

print(f"Interpolated value at x = 3.5 is {p:.6f}")
