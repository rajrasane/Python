# 11. Write a Python program to find the intersection of two given arrays using Lambda.
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]

arr1 = [1,2,3,5,7,8,9,10]
arr2 = [1,2,4,8,9]

intersection = list(filter(lambda x : x in arr2,arr1))

print(f"The intersection between these both arrays :- {intersection}")