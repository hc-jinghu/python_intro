# 繼承權

from class_and_object import dog

class Poodle(dog):
    def __init__(self, size=None, name=None):
        self.size = size
        self.name = name
        
    def print_size(self):
        print(self.size)


# create a dog
andy = Poodle("中型犬", "Andy")
bastion = Poodle()

andy.print_size()
andy.print_name()
    