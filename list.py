# There's no array for python

grades = [20, 30, 40, 50, 60]
names = ["Erin", "Jing", "Oscar"]
random_things = [True, "yes", 190]

grades[-1] = 100
print(grades[-2])
print(names[1:2]) # get element from range 1-2, excluding 2

phrase = "Hello World"
print(phrase[0:5]) # get string from 1st to 4th character


# examples of basic functions for list
grades.extend(names)
print(grades)
grades.append(True)
print(grades)
grades.insert(0,False)
print(grades)
grades.remove(100)
print(grades)
grades.pop()    # remove the last element from the list
print(grades)
grades.clear()  # remove all elements from the list
print(grades)
