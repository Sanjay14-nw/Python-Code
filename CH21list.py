student=['sanjay',18,'grade A']
print(student)
print(type(student))
print(len(student))

#sring is immutable but the list is mutable
student[0]='sanijay'

#list slicing
marks=[67,89,67,45,34,88]
print(marks[1:4])
print(marks[-3:-1])
print(marks[::-1])

#list methods
list=[5,7,3,9]
list.append(6)
print(list.sort())
print(list)
list.reverse()
print(list)

fruits=['apple','banana','cheery']
fruits.sort(reverse=True)
print(fruits)
list.pop(3)
print(list)

#function 
Num=[1,2,3,4,5,6,7,8,9]
print(min(Num),max(Num))


