class person:
    name='sanjay'
    
    def change_name(self,name):
        self.name=name
        
p1=person()
p1.change_name('rahul jangid')#it crate new attributes 
print(p1.name)  #to change the main value you have to use class method
print(person.name)     

class person1:
    name='sanjay'
    
    def changename(self,name):
        person1.name=name
        
p2=person1()     #its 1st method                
print(p2.name)
p2.changename('rahul jangid')
print(p2.name)
print(person1.name)
        
        
class  person3:
    name='naveen'
    
    @classmethod
    def changename1(cls,name):
        cls.name=name
        #it will change the value from main ohject
p3=person3()
print(p3.name)
p3.changename1('reena')
print(p3.name)
print(person3.name)        
               