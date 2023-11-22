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
            'stock' : 10
        },
        'onion': {
            'name':'Onion',
            'price':'79RS',
            'stock':15
        },
        'greenchilli':{
            'name':'Green chilli',
            'price':'46RS',
            'stock':12
        },
        'beetroot':{
            'name':'Beetroot',
            'price':'34RS',
            'stock':14
        },
        'potato':{
            'name':'Potato',
            'price':'40RS',
            'stock':16
        },
        'cabbage':{
            'name':'Cabbage',
            'price':'25RS',
            'stock': 13
        },
        'carrot':{
            'name':'Carrot',
            'price':'39RS',
            'stock':17
        
        },
        'corn':{
            'name':'Corn',
            'price':'35RS',
            'stock':19
        },
        'coconut':{
            'name':'Coconut',
            'price':'37RS',
            'stock':16
        },
        'ginger':{
            'name':'Ginger',
            'price':'111RS',
            'stock':20
        },
        'elephantyam':{
            'name':'Elephant Yam',
            'price':'34RS',
            'stock':15
        },
        


    },
    'fruits':{

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
    ch = int(input('Enter the choice : '))
    if ch == 1:
        sign_in()
        break
    elif ch == 2:
        name = input('Enter your username : ')
        create_user(name)
        
