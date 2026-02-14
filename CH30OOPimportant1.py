                                         #ABSTRACTION
#hiding the implementation details of a class and only showing the essential features to the user 
class car:
    def __init__(self):
        self.acc=False
        self.clutch=False
        
    def start(self):
        self.acc=True
        self.clutch=True
        print('car started...')
     
c1=car()
c1.start()            
                       
                         
                                         