from tabulate import tabulate

# Your database
database = {     #The Whole Database . 
    'user' : {
        'aaronshenny':{
            'name' : 'Aaron Shenny',
            'password' : '123'
        },                                            
        'user':{                         #Default user

            'name' : 'Guest',
            'password' :'root'
        },                  
        'aswinaravind27':{
            'name' : 'Aswin Aravind',    #User database
            'password':'aswi'

          
        }
    },
    'vegetables':{
        'tomato' : {
            'name' : 'Tomato',
            'price' : '48RS',
                'stock' : 10            #Vegetable Database
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
    }
}


# user_data = []
# for user, details in database['user'].items():
#     user_data.append([user, details['name'], details['password']])
# print(user_data)
# # Extracting vegetable data
# vegetable_data = []
# for veggie, details in database['vegetables'].items():
#     vegetable_data.append([veggie, details['name'], details['price'], details['stock']])
# print(vegetable_data)
vegetable_data = database.get('vegetables')
fruits_data = database.get('user')
for veg_name, veg_info in vegetable_data.items():
        vname = veg_info.get('name', 'N/A')  
        vprice = veg_info.get('price', 'N/A')                
        vstock = veg_info.get('stock', 'N/A')
        for fru_name in fruits_data:
            fname = fru_infro.get('name', 'N/A')  
            fprice = fru_infro.get('price', 'N/A')                
            
            print(f"| {vname.ljust(15)}| {vprice.ljust(6)}| {str(vstock).ljust(8)}|")

























































# # Your database
# # (Assuming you've defined 'database' as provided in the previous code)



# # Your database
# # (Assuming you've defined 'database' as provided in the previous code)

# # Extracting user data


# # Your database
# # (Assuming you've defined 'database' as provided in the previous code)

# # Extracting user data
# user_data = []
# for user, details in database['user'].items():
#     user_data.append([user, details['name'], details['password']])

# # Extracting vegetable data
# vegetable_data = []
# for veggie, details in database['vegetables'].items():
#     vegetable_data.append([veggie, details['name'], details['price'], details['stock']])

# # Create headers for tables
# user_headers = ['User', 'Name', 'Password']
# vegetable_headers = ['Vegetable', 'Name', 'Price', 'Stock']

# # Get tabulated data
# user_table = tabulate(user_data, headers=user_headers, tablefmt='plain').split('\n')
# vegetable_table = tabulate(vegetable_data, headers=vegetable_headers, tablefmt='plain').split('\n')

# # Merge and format rows into columns
# combined_table = ''
# for user_row, veggie_row in zip(user_table, vegetable_table):
#     combined_table += f"{user_row.ljust(15)}{veggie_row}\n"

# # Add header manually
# header = 'User'.ljust(15) + 'Name'.ljust(15) + 'Password'.ljust(15) + 'Vegetable'.ljust(15) + 'Name'.ljust(10) + 'Price'.ljust(10) + 'Stock'.ljust(10) + '\n'
# combined_table = header + combined_table

# print(combined_table)
