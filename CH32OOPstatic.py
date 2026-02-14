#static methods
# methods that dont use the self parameter(work at class level)
class student:
    @staticmethod #decorator  #decorators allow us to wrap another function in order to extend the cehaviour of the wrapped function ,without permanently modifying it
    def hello():
        print('hello')
        
s1=student()
s1.hello() #without @staticmethod this will give error