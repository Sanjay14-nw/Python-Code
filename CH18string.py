#creating string
a="ehh?"
b="""EHH?"""         #multiline
c='eh'
d='''ehhh'''
print(a,b,c,d)

#concept of indexing
x='sanjay'  #positive indexing, it start from 0
print(x[3]) #output is j
             #negative indexing, it start from right side  
print(x[-1]) #output is y

# Slicing 
r='pyhton is a language'
print(r[0:4])
print(r[2:8:2])
print(r[2:9:2])

print(r[2:4:-1]) #it gives empty space 
print(r[-5:-2:2])
print(r[::-1])   #it reverse the sentenses
print(r[-1:-5:-1])

#editing and deletion in strings

 #Editing is not exist in python 
 #deletion
t='hello'
print(t)
del t
# print(t) deletion also doesnt exisit in python
