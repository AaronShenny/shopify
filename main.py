import getpass
database = {
    'user' : {
        'aaronshenny':{
            'name' : 'Aaron Shenny',
            'password' : '123'
        },
        'user':{

            'name' : 'user',
            'password' :'root'

        
        }
    },
    
}
def create_user():
    print('[Sorry, Dur to the limited knowlegde, Now creating account will be deleted after the program closes. Use the default username and password]')
    print('Creating a user account..')
    name = input('Enter your username : ')
    if name in database['user']:
        print('Same user has been found in our databse. Please login ...')
    else:
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


def sign_in():
    username = input('Enter your username : ')
    try:
        if username in database['user']:
            password1 = getpass.getpass()
            try:
                if password1 == database['user'][username]['password']:
                    print('Account logined..')
                    print(f'Welcome {username}')
            except:
                print('Incorrect password')
            print('found')
    except:
        print('Account not Found')
    

while True:
    ch = int(input('Enter the choice'))
    if ch == 1:
        sign_in()
    elif ch == 2:
        create_user()