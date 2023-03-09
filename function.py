# 函式

def helloWorld():
    print("Hello World")
print("this is not part of the function anymore")
helloWorld()

def callName(name, age):
    print(name + " is " + str(age))
callName("Erin", 18)

def sum(num1, num2):
    return num1 + num2
print(sum(1,2))
# 如果return沒有值，python會預設為None

