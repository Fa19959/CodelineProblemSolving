import re

regExp_1 = '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,7}\b'
regExp_2 = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$"

username = input('Username: ')
password = input('Password: ')
email = input('Email: ')


if(username == '' or username == None  and len(username) < 50) :

    print ('Username is invalid')

else :

    print ('Username is valid')


if  (re.match(regExp_2 ,password)) :

    print ('Password is valid')

else :

    print ('Password is invalid')


if (re.match(regExp_1 ,email)):

    print ('Email is valid')

else :

    print ('Email is invalid')
