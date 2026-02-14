class Student:
    def __init__(self,fullname,chem_marks,phy_marks,math_marks):
        self.fullname=fullname
        self.chem_marks=chem_marks
        self.math_marks=math_marks
        self.phy_marks=phy_marks
        total=chem_marks+math_marks+phy_marks
        avg=total/3
        print('the average of ',fullname,'marks is',avg)
        
s1=Student('sanjay bahadur',50,50,60)  
      
        
    