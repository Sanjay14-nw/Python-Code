#Set rules
s1={1,'hello',3.44}
print(s1)
print(type(s1))

#set do not allow duplicates
sets={1,2,2,2,3}
print(sets) #it doent print(2) 3 time 


#sets have no indexing/slicing
 #sets doesnt support indexing it will give error (s1[0])
 
#sets dont allow mutable data types

 #we didnt use list in sets b/c list is mutable it shows error
 #instead of list we can use tuple b/c tuple is an immutable
s2={(1,2,3),'hello'}
print(s2) 

  #it show error when you use dict in sets


#set itself is a mutable data type
 #it can add elements in sets
s3={1,2,3,4,5}
print(s3)
print(id(s3))          #it also doesnt change it address when it get add
s3.add(7)
print(s3) 
print(id(s3))


#delete function

#del
del s2

#remove
s3.remove(3)
print(s3)

#pop
s1.pop()
print(s1)