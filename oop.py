#Object Oriented Programming in python
    #when any function is inside a class it behaves as method

class Person:  #parent class
    def __init__(self,name,age):
        self.name = name  
        self.age = age  
        
class Employee(Person): #child class
    def __init__(self,age,name, total):
        super().__init__(name,age) #inheritance from parent class
        self.total = total  
    
    def display(self):  
        print(self.name,self.age)

class Student(Person): #child class
    def __init__(self,age,name, total): 
       super().__init__(name,age) #inheritance from parent class
       self.total = total  
    
    def display(self):
        print(self.name,self.age)
    def result(self):
    #behavior of objects
        if self.total > 120:
            print('pass')
        else:
            print("fail")

        
s0 = Student(0,'hariiish bhaiiiii',180)
s0.display()
s0.result()