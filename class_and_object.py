# class 類別
# object 物件

# init() must be written as __init__
class dog:
    def __init__(self, name, breed, age, gender):
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender
    
    def print_name(self):
        print(self.name)
    def print_breed(self):
        print(self.breed)
    def print_age(self):
        print(self.age)
    

husky = dog("fluffy", "husky", 18, "female")
# print(husky.age)