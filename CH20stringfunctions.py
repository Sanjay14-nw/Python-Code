#commmon function
 #len 
a='sanjay'
print(len(a))

 #max
print(max(a)) 
 
 #min
print(min(a)) 
 #sorted
print(sorted(a)) 


#capitalize/title/upper/lower/swapcase
print(a.capitalize())
print("hello my name is balah".title())
print(a.upper())
print(a.lower())
print('ERENmikasa'.swapcase())

#count
print("it is raining".count("i"))

#find/index
print('it is raining'.find("i"))
print('it is raining'.index('rain'))

#endswith/startswith
print('it is raining'.endswith('today'))
print('it is raining'.startswith('it'))

#format
print('hello my name is {} and i am {}'.format('sanjay',20))
print('hello my name is {name} and i am {age}'.format(name='everone',age='you'))

#isalnum/isalpha/isdecimal/isdigit/isidentifier
print('hello14'.isalnum()) #isalnum means alphabets and number
print('hello'.isalpha)     #isalpha means only alphabets 
print('20'.isdigit())      #isdigit means only digit
print('hello world'.isidentifier())#isidentifier means only identifier

#split
print('who is the pm of india'.split())
print('who is the pm of india'.split('i'))

#join
print(' '.join(['who', 'is', 'the', 'pm', 'of', 'india']))
print('/'.join(['who', 'is', 'the', 'pm', 'of', 'india']))

#replace
print('hi my name is sanjay'.replace('sanjay','sanijay'))

#strip
print('       sanjay       '.strip())


