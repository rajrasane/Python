#write a python function that takes a list of words and returns the length of the longest one
list1 = []
choice = 1
def listentries(choice):
    while choice==1:
        val = input("Enter value :- ")
        list1.append(val)
        choice = int(input("Enter 1 to enter more :- "))

def listdisp(list1):
    print("\nEntered list :- \n")
    for i in range(0,len(list1)):
        print(list1[i],end=",")

def findmax(list1):
    maxl = list1[0]
    for i in range(1,len(list1)):
        if(len(maxl)<len(list1[i])):
            maxl = list1[i]
    print("Longest list item :- ",maxl)

listentries(choice)
listdisp(list1)