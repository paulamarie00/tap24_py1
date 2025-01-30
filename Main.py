# Python 1
# Basic Data Types

h = "hello"
w = "world"

print(h,w)
print(h+w)

n1 = 5
# print(h+n1)

# How to concatenate str with number?
# Typecasting 

print(h+str(n1))

"""
str() - cast to string 
int() - cast to integer
float() - cast to float
"""

# Formatted Strings 
n1 = 5
n2 = 3
res = n1 + n2
out = f"{n1}+{n2}= {n1+n2}"
print(out) 


# Logical operators
# Code Block

n1=5
n2=5
if n1<n2:
    print("Lesser")
    print("<"*6)
elif n1==n2:
    print("Equal")
    print('=====')
else:
    print("Greater")
    print(">"*len("Greater"))

# blocks in Python use indentation
# used in if statements/ function def

f = 17.4
print(type(f))


