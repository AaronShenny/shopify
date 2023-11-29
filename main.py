import getpass
import time
user_buy =  {}
database = {
    'user' : {
        'aaronshenny':{
            'name' : 'Aaron Shenny',
            'password' : '123'
        },
        'user':{

            'name' : 'Guest',
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
        'brinjal':{
            'name':'Brinjal',
            'price':'33RS',
            'stock':18

        }
        


    },
    'fruits':{

    }
}
#login  = False
def create_user(name):
    print('Sorry, Dur to the limited knowlegde, Now creating account will be deleted after the program closes. Use the default username and password...')
    print('Creating a user account...')
    username = input('Username : ')
    if username in database['user']:
        print('Same user has been found in our databse. Please login ...')
    else:
        try: 
            password = getpass.getpass(prompt = 'Create Your Account Password : ')
        except Exception as Error:
            print('Error : ', Error)
        try:
            database['user'][username] = {
                'name': name,
                'password': password
            }
        except Exception as Error:
            print('Error : ', Error)
        sign_in()


def sign_in():
    username = input('Username : ')
    if username in database['user']:
        password1 = getpass.getpass(prompt = 'Password : ')   
        if password1 == database['user'][username]['password']:
            time.sleep(1)
            print('Account logined..')
            
            print('Welcome',database['user'][username]['name'])
            
            username1 = username
            login = True

        else:
            print('Incorrect Password...')

            
    else:  
        time.sleep(1)
        print('Account not Found')
        time.sleep(1)
        print('Creating an account...')
        time.sleep(1)
        name  = input('Full name : ')
        create_user(name)
    return username

def buy(l):
    
    while True:
        item = input('Enter an item : ')
        qut = int(input(f'How much kilo you need for {item} : '))
        items = (item,qut)
        #items = tuple(input('Enter the item :'))
        print(items)
        if items[0] in database['vegetables']:
           l.append(items)
        elif items[0] == 'exit':
            break
        else:
            print('Item not Found')
        
    user_buy[username] = l
    print(user_buy)

def list1(database):
    vegetable_data = database.get('vegetables')

    if not vegetable_data:
        print("No vegetable data found!")
        return

    print("---------------------------------")
    print("| Vegetable      | Price | Stock   |")
    print("---------------------------------")

    
    for veg_name, veg_info in vegetable_data.items():
        name = veg_info.get('name', 'N/A')  
        price = veg_info.get('price', 'N/A')
        stock = veg_info.get('stock', 'N/A')

        
        print(f"| {name.ljust(15)}| {price.ljust(6)}| {str(stock).ljust(8)}|")

   
    print("---------------------------------")


# def stock_reducer():

def recipt():
    confirm =  input('Anything else ..? : ').lower()
    if confirm == 'yes':
        l =  user_buy.get(username)
        buy(l)
    brougth_items = user_buy.get(username)
    print('='*55)
    print('RECIPT'.center(50))
    print('='*55)
    for i in  brougth_items:
        print(i)


print()
print('='*55)
print()
print('\t\tWelcome to Shenny \'shop\'!')
print()
print('='*55)
print()
time.sleep(1)

while True:
    time.sleep(1)
    username = sign_in()    
    break
    login = True
        #print(database)
#print(database)

#buy()
# if login != True:
#     sign_in()
time.sleep(1)
list1(database)
buyacceot =  input('Wanna buy something from our store ...?? [yes/no] : ').lower()
if buyacceot == 'yes':
    time.sleep(1)
    l = []
    buy(l)
    recipt()
else:
    time.sleep(1)
    print('Thank you for comming')
    time.sleep(5)

# import shutil
# import os
# # Get the current working directory
# cwd = os.getcwd()

# # Get the path to the existing file
# file_path = os.path.join(cwd, "my_file.py")

# # Copy the file to itself
# shutil.copy(file_path, file_path)
print(user_buy)