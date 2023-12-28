import getpass   #Prompt the user for a password without echoing
import time      #This module provides various time-related functions
user_buy =  {}   #Intializong a variable

database = {     #The Whole Database . 
    'user' : {
        'aaronshenny':{
            'name' : 'Aaron Shenny',
            'password' : '123'
        },                                            
        'user':{                                      #userdata

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
            'stock':14                               #vegetable database
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
def create_user(name):                   #This Function used to create user into the database
    print()
    print()
    print('SIGN-UP')
    print('Sorry, Due to the limited knowlegde, Now creating account will be deleted after the program closes. Use the default username and password...')
    print('Creating a user account...')
    username = input('Username : ')
    if username in database['user']:  #This will check if the user had already created account
        print('Same user has been found in our databse. Please login ...')
        
    else:
        try: 
            password = getpass.getpass(prompt = 'Create Your Account Password : ')   
        except Exception as Error:
            print('Error : ', Error)
        try:
            database['user'][username] = {
                'name': name,                            #Adds Name and password into the database
                'password': password
            }
        except Exception as Error:
            print('Error : ', Error)                   
def sign_in():                                           #Function that helps to sign in to their account
    #login = False
    while True:
        print()
        print()
        print('\t\t\tLOGIN')
        print()
        username = input('Username : ')
        if username in database['user']:                 #Checking given Username is matching with usernames in databse
            password1 = getpass.getpass(prompt = 'Password : ')   
            if password1 == database['user'][username]['password']:    #Checking if the given password is correct with database
                time.sleep(1)
                print('Account logined..')
                print('Welcome',database['user'][username]['name'])
                username1 = username
                login = True  #Intializing the varible as True
                return username,login #Returning username and login variable 
                break
            else:
                login = False #Intializing the varible as True
                print('Incorrect Password...')
                login_checker(login)   
                return username,login  #Returning username and login variable 
        else:  
            time.sleep(1)
            print('Account not Found')
            time.sleep(1)   #If the account didnt found on the database then create_user() is called
            print('Creating an account...')
            time.sleep(1)
            name  = input('Full name : ')
            create_user(name)
       
def buy(l,username): #Function that helps user to buy products
    brougth_items = []
    print('Type  "0" or "exit" after finishing adding the products')
    while True:
        item = input('Enter an item : ').lower() #User enters the product they need
        if item == 'exit' or item == '0': #To exit the while loop
            break
        elif item in brougth_items:
            print()                      #Checking the cart if the user had already brougtj
            print('Item is already in the cart!!')
            for i in l:
                if item.title() == i[0]: 
                    print(f'Product{i[0]}')
                    print(f'Quantity : {i[1]}') 
            change = input('Do you want to change the quantity  ? : [yes/no] ')  #Asking user if they need to change the quantity
            if change == 'yes':
                for i in l:
                    if item.title() == i[0]:
                        product,quantity = i   
                        quantity = float(input(f'How much kilo you need for {database["vegetables"][item]["name"]} : ')) 
                        t = product,quantity
                        l.remove(i)
                        l.append(t)
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
                        if qut < 0:
                            print('The digit should be more than 0')
                            buy(l,username)
                            break
                        if qut > database['vegetables'][item]['stock']:
                            print(f'The digit should be less than the TOTAL STOCK, Remaining Stock : {database["vegetables"][item]["stock"]}')
                            buy(l,username)
                            break

                        brougth_items.append(item) 
                        items = (database['vegetables'][item]['name'],qut)
                        l.append(items)

                        database['vegetables'][item]['stock'] = database['vegetables'][item]['stock'] - qut

                        print(f"Remaing Stocks = {database['vegetables'][item]['stock']}")

                        if database['vegetables'][item]['stock'] == 0:
                            del database['vegetables'][item]
                        #stock_reducer(item,qut)
                    else:
                        print('Item not Found')
                except ValueError:
                    print('Please enter an valid value...')
   
    user_buy[username] = l
    print(user_buy)
    return user_buy

def list1(database):
    vegetable_data = database.get('vegetables')

    if not vegetable_data:
        print("No vegetable data found!")
        return

    print("------------------------------------")
    print("| Vegetable      | Price | Stock   |")
    print("------------------------------------")

    
    for veg_name, veg_info in vegetable_data.items():
        name = veg_info.get('name', 'N/A')  
        price = veg_info.get('price', 'N/A')
        stock = veg_info.get('stock', 'N/A')

        
        print(f"| {name.ljust(15)}| {price.ljust(6)}| {str(stock).ljust(8)}|")

   
    print("--------------------------------")

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
print('  / ____| |  | |/ __ \|  __ \_   _|  ____\ \   / /')     
print(' | (___ | |__| | |  | | |__) || | | |__   \ \_/ / ')    
print('  \___ \|  __  | |  | |  ___/ | | |  __|   \   /  ')     
print('  ____) | |  | | |__| | |    _| |_| |       | |   ')
print(' |_____/|_|  |_|\____/|_|   |_____|_|       |_|   ')
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

        print('Test pass 2')
        time.sleep(1)
        list1(database)
        buyacceot =  input('Wanna buy something from our store ...?? [yes/no] : ').lower()
        if buyacceot == 'yes':
            time.sleep(1)
            l = []
            buy(l,username)
            if user_buy[username] == []:
                pass
            else:
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