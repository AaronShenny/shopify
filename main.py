import getpass
database = {
    'user' : {
        'aaronshenny':{
            'name' : 'Aaron Shenny',
            'password' : '123'
        },
        'user':{
            name : 'user',
            password :'root'
        },
        'user1':{
            name : 'user1',
            password :'root1'
        }
    }
}





def create_user():
    print('[Sorry, Dur to the limited knowlegde, Now creating account will be deleted after the program closes. Use the default username and password]')
    print('Creating a user account..')
    name = input('Enter your username : ')
    try: 
        password = getpass.getpass()
    except Exception as Error:
        print('Error : ', Error)
    try:
        database['user'][name] = {
            'name': name,
            'password': password
        }
    except Exception as Error:
        print('Error : ', Error)
print(database)
create_user()
print(database)
