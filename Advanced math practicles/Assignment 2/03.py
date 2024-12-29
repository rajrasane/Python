# Write a Python program to sort a list of tuples using Lambda.

ls = [("English",45),("Math",43),("Geography",47),("Biology",41)]

print(sorted(ls,key = lambda x : x[1]))