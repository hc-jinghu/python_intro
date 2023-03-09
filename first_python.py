# first python program
print("Hello World!")

# define variable
# variable can't begin with number 
quote = "hello world"
print(quote)
print("This line will print \n" + "\"" + quote + "\"") 

temp = 50
print(temp)
temp = "green"
print(temp)

# function (built-in function example)
print(temp.upper())
print(temp.isupper())
print(temp.lower().islower())
# index
name = "apple"
print(name[1])
print(name.index("a"))
# replace
print(name.replace('a','A'))

# number
from math import *
print(7/4)
print(7//4) # round to nearest integer 無條件捨去
print(floor(7/4)) # 無條件捨去 to nearest integer
print(round(7/4)) # 四捨五入 to nearest integer

