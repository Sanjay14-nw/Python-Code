class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.phy+self.chem+self.math)/3)+'%'
        
s1=student(67,78,89)
print(s1.percentage)   #but if we change the number it will show old output to solve this situtaion we have to use property method 

class student1:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+'%'  
    
s2=student1(56,67,78)
print(s2.percentage)    
s2.phy=34
print(s2.percentage)

#it also have two more decoreter 
#gether
#setter