class calci:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        print(f"Addition of two elements is :- {self.a+self.b}")

    def sub(self):
        print(f"Subtraction of two elements is :- {self.a-self.b}")

    def div(self):
        print(f"Division of two elements is :- {round(self.a/self.b,2)}")

    def mul(self):
        print(f"Multiplication of two elements is :- {self.a*self.b}")

obj = calci(4,2)

print("*****Menu*****")
print("0.Exit")
print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")

while(1):
    print()
    ch = int(input("Enter your choice :- "))

    if(ch==0):
        print("exiting...")
        print()
        exit(0)
    elif(ch==1):
        obj.add()
    elif(ch==2):
        obj.sub()
    elif(ch==3):
        obj.div()
    elif(ch==4):
        obj.mul()
    else:
        print("Invalid Choice!")
    