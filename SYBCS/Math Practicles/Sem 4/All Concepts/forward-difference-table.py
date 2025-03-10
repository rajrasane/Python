import numpy as np

n = int(input("Enter number of data points: "))

x = np.zeros(n)
y = np.zeros((n, n))

print("Enter data for x and y:")
for i in range(n):
    x[i] = float(input(f"x[{i}] = "))
    y[i][0] = float(input(f"y[{i}] = "))

# Compute forward difference table
for i in range(1, n):  # Columns
    for j in range(n - i):  # Rows
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1]


# Print forward difference table
print("\nForward Difference Table:\n")
for i in range(n):
    print(f"{x[i]:.2f}", end=" ")  # Print x values
    for j in range(n - i):  # Print only valid y values
        print(f"| {y[i][j]:.2f}", end=" ")
    print()  