#arithimetic op 

print("hello"+"world")
print("*"*50)
print(' hello '*5)


#relation op 
print('hello'=='world')
print('hello'!='world')

 #lexiographically
print('mumbai' > 'pune')
print('kolkata' > 'goa')
print('K'<'k')

#logicial op
print("hello" and 'world')
#" "==false                      #ek bhi false to false
#"hello"== true
print(''and'hello')
print(''or'world')              #ek bhi true to sab true
print('world'or'hello')
print(not 'hello')

#loops 
c='hello my world'
for i in c[2:7:2]:
    print(i)

# name=str(input("enter your name:")) for just fun
# for i in name[::-1]:
#     print(i,end='')
    
#membership op
print('h' in c)