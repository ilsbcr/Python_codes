

import random 


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
                print("Enter 1 or 2 to select options ")
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
    length = int(input("Enter the length"))
    lowercase_uppercase = bool(input("Include lowercase and uppercase letters y/n"))
    Numbers = bool(input("Include numbers y/n"))
    Symbols = bool(input("Include Symbols y/n"))
    
    Password = Generate(l=length,ul=lowercase_uppercase,n=Numbers,sy=Symbols)
    return Password

# Arbitrary Keyword Arguments
def Generate(**p) :
    print(p["l"] , p["ul"] ,  p["n"] , p["sy"])
    list_numbers = [1,2,3,4,5,6,7,8,9]
    list_alpha_lowercase = []
    list_alpha_uppercase = []
    list_symbols = []
    Password = '123'
    return Password 

# Main program 
while True : 
    choice = display_menu()

    if choice == 1 :
        G_default_pass() 
    elif choice == 2 :
        G_custom_pass()
    else :
        break

print("Programe ended")