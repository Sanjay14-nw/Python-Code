dict={
    'name':'sanjay',
    'age': 32,
    'marks': 72,
    'college':'citm'
}

print(dict['name'])
print(dict['college'])
print(dict['age'])
dict['name']='sanijay'
dict['surename']='bahadur'
print(dict)

#null dictinary
null={}
print(null)
null['something']='nothing' 
print(null)

#nested dictinary
student={
    'name':'sanjay',
    'subject':{
        'chem':66,
        'phy':88,
        'math':89
    }
}
print(student)
print(student['subject']['chem'])

#dict method
print(student.keys()) #return all keys
print(student.values())#return all values
print(student.items())#reurns all (key,val) pair as tuples
print(student.get('keys')) #returns the key according to value
print(student.update({'surename':'bahadur'})) # inserts the specified items to the dictionary
print(student)