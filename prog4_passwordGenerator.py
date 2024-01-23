

import random 
import string

def display_menu():
    while True :
        print("Menu")
        print("1-Generate a password with default setting ")
        print("2-Generate a password with custom setting ")
        print("3-Exit")
        try :
            choice = int(input("Choose an option : "))
            if 1 <= choice <= 3 :
                return choice
            else : 
                print("Message : Enter 1 or 2 to select options \n")
        except ValueError : 
            print("Enter a valid choice (integer) ")
        
def G_default_pass() : 
    print("Default password generation")
    print("length  = 13 | Contain lowercase_uppercase | Contain Numbers | Contain Symbols ")
    length = 13 
    lowercase_uppercase = True 
    Numbers = True
    Symbols = True

    Password = Generate(l=length,ul=lowercase_uppercase,n=Numbers,sy=Symbols)
    return Password
    

def G_custom_pass() : 
    print("Custom password generation")
    length = int(input("Enter the length :"))
    lowercase_uppercase = bool(input("Include lowercase and uppercase letters Enter 1 or 0 :"))
    Numbers = bool(input("Include numbers Enter 1 or 0 :"))
    Symbols = bool(input("Include Symbols Enter 1 or 0 :"))
    
    Password = Generate(l=length,ul=lowercase_uppercase,n=Numbers,sy=Symbols)
    return Password

# Arbitrary Keyword Arguments
def Generate(**p) :
    #print(type(p["l"]) , type(p["ul"]) ,  type(p["n"]) , type(p["sy"]))
    list_numbers = [1,2,3,4,5,6,7,8,9]
    list_alpha_lowercase = list(string.ascii_lowercase)
    list_alpha_uppercase = list(string.ascii_uppercase)
    list_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', ',', '.', '<', '>', '/', '?']
    list_all = list_numbers + list_alpha_lowercase + list_alpha_uppercase + list_symbols
    Password = " "
    

    #print(list_all)
    for i in range(p['l']) : 
       #print("Boucle")
        
        r = random.randint(1,5)
        if  r == 1 :
            Password = Password + str(random.choice(list_numbers)) 
        elif r == 2 :
            Password = Password + str(random.choice(list_alpha_lowercase)) 
        elif r == 3 :
            Password = Password + str(random.choice(list_alpha_uppercase))
        elif r == 4 :
            Password = Password + str(random.choice(list_symbols)) 
        else : 
            Password = Password + str(random.choice(list_all))
       
            
         
    return Password 

# Main program 
#filep = open("pw.txt","a")
while True : 
    choice = display_menu()

    if choice == 1 :
       print("The password :" , G_default_pass(),type(G_default_pass())) 
       #filep.write(G_default_pass())
      # filep.newlines
        
    elif choice == 2 :
         print("The password :" , G_custom_pass())
    else :
        break

print("Programe ended")
#filep.close