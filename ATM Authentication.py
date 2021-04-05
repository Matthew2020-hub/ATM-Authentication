#register
# - first name, last name, password, email
# - generaten user account


#login
# - account number & password


#bank operations

#Initializing the system
import random

database = {} #dictionary

def init():

   
    print("Welcome to bankPHP")
 
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        
        login()
    elif(haveAccount == 2):
        
        register()
    else:
        print("You have selected invalid option")
        init()


def login():
    
    print("Welcome our highly esteemed customer")

    accountNumberFromUser = int(input("Enter your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
               
                
    print('What do you want to do?')
    loginOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if(loginOption == 1):
                
            depositOperation()
    elif(loginOption == 2):
                
            withdrawalOperation()
    elif(loginOption == 3):
            
            logout()
    elif(loginOption == 4):
            
            exit()
    
        


def register():

    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def bankOperation(user):

    print(f"Welcome {user[0]} {user[1]}")

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
        
        depositOperation()
    elif(selectedOption == 2):
        
        withdrawalOperation()
    elif(selectedOption == 3):
        
        logout()
    elif(selectedOption == 4):
        
        exit()
    else:
      
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
     withdrawal= int(input ('How much would you like to withdraw \n'))
     print('Take your cash')
     withdrawOption = int(input("Do you still want to withdraw more cash? (1) yes (2) no \n"))
     
     if (withdrawOption == 1):
        withdrawalOperation()
     else:
         print("Thanks for banking with us...")
         init()
    

        
     

def depositOperation():
    deposit = 0
    deposit1 = int(input("How much would you like to deposit?\n") )

    print(f"You have deposited {deposit1}")
    deposit2 =int(input("would you like to perform more operation? (1) yes (2) no \n"))

    if (deposit2 == 1):
        login()
    else:
        print("Thanks for banking with us")
    init()


def generationAccountNumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()

#### ACTUAL BANKING SYSTEM #####

init()