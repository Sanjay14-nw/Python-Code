class circle:
     def __init__(self,radius):
         self.radius=radius
         
     def area(self):
         return self.radius*self.radius*3.14    
     
     def perimeter(self):
         return self.radius*2*3.14
     
     
r1=circle(4)
print(r1.area())
print(r1.perimeter())