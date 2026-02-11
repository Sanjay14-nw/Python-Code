#WAp to ask the user to enter names of their 3 favorite movies and store them in a list

movie=[]
mov1=(input('enter 1st movie:'))
mov2=(input('enter 2nd movie:'))
mov3=(input('enter 3rd movie:'))

movie.append(mov1)
movie.append(mov2)
movie.append(mov3)
print(movie)

#WAp to check if a list contains a palindrome of elements (hint'use copy() method')t
list=[1,2,1]
cplist=list.copy()
cplist.reverse()
if cplist == list:
    print('palimdrome')
else:
    print('not palimdrome')    
    

