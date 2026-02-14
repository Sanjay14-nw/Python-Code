  #to map with real world scenarios , we started using objects in code.
   # this is callled object oriented programming

# class students:           #this is how a class is created 
#     name='sanjay'
#     roll_no='42'
    
# St=students()            #this is how a object is created
# print(St.name)
# print(St.roll_no)

# class car:
#     colour='black'
#     size='4x4'
    
# car1=car()
# print(car1.colour)        

                     #__init__ function
                     
class student:
    
    def welcome(self):
        print('welcome students')
          
    #default constructors
    def __init__(self):
        pass
    
    #this is a class attributes
    college_name='CITM'#if you want to make college name similiar for all
    
    #parameterized constructors
    def __init__(self,fullname,marks):
        self.fullname=fullname  #this is objects attributes
        self.marks=marks
        print('adding new student in database..')
    
      
s1=student('sanjay bahadur',20)
print(s1.fullname,s1.marks)

s2=student('karan aujla',32)
print(s2.fullname,s2.marks,s2.college_name)
print(s2.welcome())   

#del keyword
del s2.fullname #this will delete the fullname object from fn.
     
        
                             