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
        },
        'aswinaravind27':{
            'name' : 'Aswin Aravind',
            'password':'aswi'

          
        }
    },
    'vegetables':{
        'tomato' : {
            'name' : 'Tomato',
            'price' : '48RS',
            'stock' : '10'
        }

    }
    
}
def create_user(name):
    print('[Sorry, Dur to the limited knowlegde, Now creating account will be deleted after the program closes. Use the default username and password]')
    print('Creating a user account..')
    #name = input('Enter your username : ')
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
    if username in database['user']:
        password1 = getpass.getpass()   
        if password1 == database['user'][username]['password']:
            print('Account logined..')
            print(f'Welcome {username}')
        else:
            print('Incorrect Password...')
    else:  
        print('Account not Found')
        print('Create an account...')
        create_user(username)


login = False

while True:
    ch = int(input('Enter the choice'))
    if ch == 1:
        sign_in()
        break
    elif ch == 2:
        name = input('Enter your username : ')
        create_user(name)
        
