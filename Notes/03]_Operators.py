# Operators

# 1) Arithmetic Operators

x = 10
y = 5

print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y) # Exponentiation
print(x // y) # Floor Division

# ---------------------------------------------------------------------------------------------------------------------------------------

# 2)  Comparison Operators

print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to

# ---------------------------------------------------------------------------------------------------------------------------------------

# 3) Logical Operators

print(x > 5 and y < 10)  # and
print(x > 5 or y < 5)    # or
print(not(x > 5 and y < 10))  # not

# ---------------------------------------------------------------------------------------------------------------------------------------

# 4) Assignment Operators

x = 10
x += 5  # x = x + 5
x -= 5  # x = x - 5
x *= 5  # x = x * 5
x /= 5  # x = x / 5
x %= 5  # x = x % 5
x **= 5 # x = x ** 5
x //= 5 # x = x // 5

# ---------------------------------------------------------------------------------------------------------------------------------------

# 5) Bitwise Operators

x = 5  # 0b0101
y = 3  # 0b0011

print(x & y)  # AND
print(x | y)  # OR
print(x ^ y)  # XOR
print(~x)     # NOT
print(x << 1) # Zero fill left shift
print(x >> 1) # Signed right shift