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
        'green chilli':{
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
        'apple':{
            'name':'Apple',
            'price':'190Rs',
            'stock':21
        },
        'banana':{
            'name':'Banana',
            'price':'55Rs',
            'stock': 24
        },
        'orange':{
            'name':'Orange',
            'price':'65Rs',
            'stock':27
        },
        'mango':{
            'name':'Mango',
            'price':'89Rs',
            'stock':13
        },
        'watermelon':{
            'name':'Watermelon',
            'price':'28Rs',
            'stock':28
        },
        'grapes':{
            'name':'Grapes',
            'price':'150Rs',
            'stock':12
        },
        'papaya':{
            'name':'Papaya',
            'price':'35Rs',
            'stock':19
        },
        'guava':{
            'name':'Guava',
            'price':'89Rs',
            'stock':11
        },
        'pineapple':{
            'name':'Pineapple',
            'price':'35Rs',
            'stock':27
        },
        'pomegranate':{
            'name':'Pomegranate',
            'price':'189Rs',
            'stock':30
        },
        'avocado':{
            'name':'Avocado',
            'price':'260Rs',
            'stock':32
        },
        'dragonfruit':{
            'name':'Dragonfruit',
            'price':'299Rs',
            'stock':31
        
        }
    }
}
total_amount = 0
brougth_items = [('Apple', 2.0), ('Green chilli', 2.0), ('Dragonfruit', 3.0), ('Elephant Yam', 4.0), ('Cabbage', 3.0), ('Banana', 3.0)]
print(''.ljust(8),'ITEM'.ljust(19),'RATE'.ljust(14),'QUANTITY'.ljust(17),'TOTAL')
for i in  brougth_items:
        product_name, quantity = i
        price_per_kilo = 0

        # Check if the product is a vegetable or a fruit
        if product_name.lower() in database['vegetables']:
            price_per_kilo = float(database['vegetables'][product_name.lower()]['price'][:-2])  # Extract price per kilo
        elif product_name.lower() in database['fruits']:
            price_per_kilo = float(database['fruits'][product_name.lower()]['price'][:-2])  # Extract price per kilo

        total_price = price_per_kilo * quantity
        total_amount += total_price

        print(product_name.ljust(20) ,'|'.ljust(3),str(price_per_kilo).ljust(5), " RS/kg".ljust(8) ,'|'.ljust(4),str(quantity).ljust(3) ," kg".ljust(6) ,'|'.ljust(3) ,str(total_price).ljust(5) , " RS".ljust(20))
print('=' * 70)