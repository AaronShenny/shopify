
# Vegetable & Fruit Store Management System

## Program Overview:
This program is a vegetable and fruit store management system developed by a group of 5 students. It facilitates user account creation, login, purchase of vegetables, and viewing of purchase receipts.

## Code Description:
### Variable Initialization:
1. **user_buy** : Stores user purchases.
2. **database**: Contains user information, vegetables, and fruits.
3. **login** : Stores user login information.
4. **username** : Stores username
5. many more...

### Functions:
#### **create_user(name)**:
1. **Purpose**: Creates a new user account.
2. **Parameters**: name (Full name of the user).
3. **Description**: Handles account creation by prompting users for a username and password.
#### **sign_in()**:

1. **Purpose** : Manages user sign-in functionality.
2. **Description**: Allows existing users to log in by verifying their username and password.

#### **buy(l, username)**:

1. **Purpose**: Enables users to purchase items.
2. **Parameters**: l (List for storing purchased items), username (User's username).
3. **Description**: Handles the purchase process, updates stock, and manages the user's cart.

#### **list1(database)**:

1. **Purpose**: Lists available vegetables with their prices and stocks.
2. **Parameters**: database (Contains vegetable data).
3. **Description**: Prints a formatted list of available vegetables and their details.
#### **receipt(username)**:

1. **Purpose**: Generates a receipt for the user's purchases.
2. **Parameters**: username (User's username).
Description: Prints a receipt containing the purchased items and relevant details.
#### **login_checker(login)**:

1. **Purpose**: Checks the user's login status.
2. **Parameters**: login (Login status).
3. **Description**: Validates the login status and prompts for sign-in if not logged in.
#### **main()**:

1. **Purpose**: Controls the main program loop.
2. **Parameters**: None.
3. **Description**: Manages the user interaction flow by handling sign-in, purchasing, and exiting the program.