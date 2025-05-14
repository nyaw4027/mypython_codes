name = {'age':22, 'student':'Ama'}
# print(name['student'])
# name['student'] ='Kofi' 
# pop() retreives the value of a key,
#  delete item from the dictionary
# name.pop('age')
# popitem() retreives and removes the last key/value pair
# inserted into the dictionary
# name.popitem()
# print('age'in name) in checks if a key exist in a dictionary
# print(list(name.keys())) retreives all the keys
# print(list(name.values())) retrevies all the values
# name['course'] ='programming' to add a new key/value to a dictionary
# print(name)


#Dictionary in a dictionary or nested dictionary

students ={
    'Business':{
        
        'firstName': 'Ama',
        'lastName': 'Nyaniba',
        'location': 'Odorko official town',
        'phoneNum': '+233571417007'
    },
    'Science':{
        'firstName': 'Varelia',
        'lastName': 'Pinto',
        'location': 'Taifa Burkina',
        'phoneNum': '+233241266413'
    },
    'Arts':{
        'firstName': 'Rachael',
        'lastName': 'Johnson',
        'location': 'Tema New Town',
        'phoneNum': '+233558040216'
    },


}

for studentName, student in students.items():
    print(f"\nDetails: {studentName}")
    full_name = f"{student['firstName']} {student['lastName']}"
    location  = student['location']
    phoneNum = student['phoneNum']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tPhone number: {phoneNum.title()}") 
