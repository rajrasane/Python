# Generate all relatively prime nos to 111 which are less than 150

import math as m

def phi(n):
    for i in range(1, n):
        if m.gcd(n, i) == 1:
            print(i)

phi(111)
