# Write a python program a square and cube every number in given list of integers using lambda

ls = [1,2,3,4,5,6,7,8,9,10]

sqr_ls = list(map(lambda x : (x**2),ls))
cube_ls = list(map(lambda x : (x**3),ls))

print(sqr_ls)
print(cube_ls)