import getpass
import time
import sys
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
        'elephant yam':{
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
def create_user(name):
    print()
    print()
    print('SIGN-UP')
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
        

def sign_in():
    #login = False
    while True:
        print()
        print()
        print('\t\t\tLOGIN')
        print()
        username = input('Username : ')
        if username in database['user']:
            password1 = getpass.getpass(prompt = 'Password : ')   
            if password1 == database['user'][username]['password']:
                time.sleep(1)
                print('Account logined..')
                print('Welcome',database['user'][username]['name'])
                username1 = username
                login = True
                return username,login
                break
            else:
                login = False
                print('Incorrect Password...')
                login_checker(login)
                return username,login
        else:  
            time.sleep(1)
            print('Account not Found')
            time.sleep(1)
            print('Creating an account...')
            time.sleep(1)
            name  = input('Full name : ')
            create_user(name)
        #print(username,login)




def buy(l,username):
    brougth_items = []
    while True:
        item = input('Enter an item : ')
        if item == 'exit' or item == '0':
            break
        elif item in brougth_items:
            print()
            print('Item is already in the cart!!')
        else:
            
            print(l)
            for i in l:
                if item in i[0]:
                    print()
                    print('Item is already added')
            else:
                try:
                    if item in database['vegetables']:
                        qut = float(input(f'How much kilo you need for {database["vegetables"][item]["name"]} : '))
                        brougth_items.append(item) 
                        items = (database['vegetables'][item]['name'],qut)
                        l.append(items)
                    else:
                        print('Item not Found')
                except ValueError:
                    print('Please enter an valid value...')

       
        
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

def recipt(username):
    print('Test Pass 5')
    confirm =  input('Anything else ..? : ').lower()
    if confirm == 'yes':
        l =  user_buy.get(username)
        buy(l)
    brougth_items = user_buy.get(username)
    print('='*55)
    print('RECIPT'.center(50))
    print('='*55)
    for i in  brougth_items:
        for j in i:
            print(j,end=' ')
        print()
def login_checker(login):
    print('Test pass4')
    if login != True:
        sign_in()

print()
print('='*55)
print()
print('\t\t\tSHOPIFY')
print()
print('='*55)

time.sleep(1)
n=0
def main():
    username = None
    while True:
        time.sleep(1)
        print('Test pass1')

        username,login = sign_in() 
    
    
        
#login = True
        #print(database)
#print(database)

#buy()
        print('Test pass 2')
        time.sleep(1)
        list1(database)
        buyacceot =  input('Wanna buy something from our store ...?? [yes/no] : ').lower()
        if buyacceot == 'yes':
            time.sleep(1)
            l = []
            buy(l,username)
            recipt(username)
        else:
            time.sleep(1)
            print('Thank you for comming')
            time.sleep(5)

        # import shutil
        # import os
        # # Get the current working directory
        # cwd = os.getcwd()

        # # Get the path to the existing file
    # fi    le_path = os.path.join(cwd, "my_file.py")

    # # Copy the file to itself
    # shutil.copy(file_path, file_path)
        print(user_buy)
        break
        # print('NEXT CUSTOMER PLEASE...')
        # time.sleep(2)

#sys.exit(ord('q'))
if __name__ == "__main__":
    main()
    while True:
        time.sleep(2)
        choice = input("Press 'q' to quit or any other key to continue shopping...: ")
        if choice.lower() == 'q':
            print('Thank you for coming\nVisit again!!')
            print("Exiting the program...")
            break
        else:
            print('NEXT CUSTOMER PLEASE...')
            time.sleep(2)
            main()