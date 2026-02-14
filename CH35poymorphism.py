class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img 
         
    def shownumber(self):
        print(self.real,'i +',self.img,'j')
        
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return complex(newreal,newimg)
    
    def __sub__(self,num2):
        newreal=self.real-num2.real
        newimg=self.img-num2.img
        return complex(newreal,newimg)
    
num1=complex(2,3)
num1.shownumber()

num2=complex(2,5)
num2.shownumber()    

num3=num1+num2
num3.shownumber()

num3=num1-num2
num3.shownumber()