# Python code to demonstrate how parent constructors
# are called.
  
# parent class
class Person(object):
  
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
  
    def display(self):
        print(self.name)
        print(self.idnumber)
          
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        
#child class
class Employee:
    def __init__(self,name,idnumber, post):
        self.name=name
        self.idnumber=idnumber
        self.post=post

        Person.__init__(self,name, idnumber)

    def details(self):
        print("My name is {}" .format(self.name))
        print("IdNumber is {}".format(self.idnumber))
        print("Post: {}".format(self.post))
a =Employee("rahmat",1 , "Assistance software developer")
a.details()
a.details()
