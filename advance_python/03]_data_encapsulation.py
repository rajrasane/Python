# Data Encapsulation (also refered as data hiding) 

# - it is generally used to hide the data information from the user.
# - includes internal object details ,such as data members , internal working.
# - maintains data integrity and restricted access to class member.
# - main work is that it combines the data and functions into single unit.

#---------------------------------------------------------------------------------------------------------------------------------------

# applying data hiding

# - for using it , we use '__'(double underscore) as a prefix before the variable .

#---------------------------------------------------------------------------------------------------------------------------------------

# for e.g
class sample:
    __a = 10
    b = 20

s1 = sample()

print(f"Value of a is {s1.__a}")          # :- This line will generate error because the variable is encapsulated using '__' and hence is inaccesible outside the class 
print(f"Value of b is {s1.b}")