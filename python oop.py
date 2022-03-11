class Rectangle:
    sides=4
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        print("Area:",self.length*self.breadth)
my_rectangle=Rectangle(4,5)
#my_rectangle.area()




#inheritance
class Mother():
    def __init__(self,fname,sname):
        self.firstname=fname
        self.surname=sname
    def nameprint(self):
        print("Name:",self.firstname+" "+self.surname)
class Child(Mother):
    pass



class Circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        return 3.14*self.r*self.r
c=Circle(5)




#another inheritance
class Bird:
    
    def intro(self):
        print("There are many types of birds.")
  
    def flight(self):
        print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):
    
    def flight(self):
        print("Sparrows can fly.")
  
class ostrich(Bird):
  
    def flight(self):
        print("Ostriches cannot fly.")
        
        
        
        