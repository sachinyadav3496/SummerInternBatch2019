def add(a,b):
    return a+b

def sub(a,b):
    return a-b

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def change(self):
        self.name = input("Enter your name : ")
        self.age = int(input("Enter your age : "))
    def show(self):
        print("The name is : ",self.name)
        print("The age is : ",self.age)
