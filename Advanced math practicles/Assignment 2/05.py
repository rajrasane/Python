# Write a python program to filter a list of integers using lambda

ls = [1,2,3,4,5,6,7,8,9,10]

def filterls():
    odd_ls = list(filter(lambda x:(x%2!=0),ls))
    even_ls = list(filter(lambda x : (x%2==0),ls))

    print(odd_ls)
    print(even_ls)


filterls()