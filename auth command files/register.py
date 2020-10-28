numofUsers = 0
userDatabase = {}
print(
    '''
    Name and Password Parameters are as follows:
    -Something easy to remember
    -Something difficult to guess

    This platform currently has zero (0) methods of password security
    '''
)
name = input('Please write your name: ')
password = input('Please write your password: ')

numofUsers += 1

userDatabase.update({name:password})

for i in userDatabase:
    print(i)
    print(numofUsers)