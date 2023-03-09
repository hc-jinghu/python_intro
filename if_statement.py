lunch = False
parents = False
"""
if lunch:
    print("Have lunch with Erin")
elif parents:
    print("Have lunch with parents")
else:
    print("餓肚子吧你")
"""

score = 100
absent = False
if not(absent) and score >= 100:
    print(score)
elif score < 100:
    print("score is less than 100")
else:
    print("score")

# using if statement in a function
def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(2,3,5))
