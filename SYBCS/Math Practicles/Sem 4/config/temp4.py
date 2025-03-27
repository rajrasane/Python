x = [0, 1, 2, 3]
y = [[1], [0], [1], [10]]

for i in range(1, 4):
    for j in range(4 - i):
        y[j].append(y[j+1][i-1] - y[j][i-1])

u = 1.5
p = y[0][0]
fact = 1
term = 1

for i in range(1, 4):
    term *= (u - (i - 1))
    fact *= i
    p += (term / fact) * y[0][i]

print(f"Interpolated value at x = 1.5 is {p:.6f}")
