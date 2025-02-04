# 2. Write a program to check if a character is a vowel.

vow = ['a','e','i','o','u']
def checkvow(a,vow):
    for i in vow:
        if(a==i):
            print("Given character is a vowel")


checkvow('b',vow)