# to print "python is bad" and "python is wonderful" where 'wonderfull' is global and 'bad' is local

n1 = "wonderful"

def disp():
    n2 = "bad"
    print(f"python is {n1}")
    print(f"python is {n2}")

disp()

