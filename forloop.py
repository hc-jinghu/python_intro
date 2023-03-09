# for迴圈

# Practice: write a function that mimics pow()
# use pow()
print(pow(2,6))

# use for loop
def power(base, power):
    result = base
    for index in range(power-1):
        result = result*base
    return result
print(power(2,6))