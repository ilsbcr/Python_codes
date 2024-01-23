

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
    lowercase = True 
    uppercase = True 
    Numbers = True
    Symbols = True

    Password = Generate(l=length,up=uppercase,lo=lowercase,n=Numbers,sy=Symbols)
    return Password
    

def G_custom_pass() : 
    print("Custom password generation")
    length = int(input("Enter the length :"))
    lowercase = bool(int(input("Include lowercase letters Enter 1 or 0 :")))
    uppercase = bool(int(input("Include uppercase letters Enter 1 or 0 :")))
    Numbers = bool(int(input("Include numbers Enter 1 or 0 :")))
    Symbols = bool(int(input("Include Symbols Enter 1 or 0 :")))
    
    Password = Generate(l=length,up=uppercase,lo=lowercase,n=Numbers,sy=Symbols)
    return Password

# Arbitrary Keyword Arguments
def Generate(**p) :
    #print(type(p["l"]) , type(p["up"]) , type(p["lo"]) ,  type(p["n"]) , type(p["sy"]))
    print(p["l"] , p["up"] , p["lo"] , p["n"] , p["sy"])
    list_numbers = [1,2,3,4,5,6,7,8,9]
    list_alpha_lowercase = list(string.ascii_lowercase)
    list_alpha_uppercase = list(string.ascii_uppercase)
    list_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', ',', '.', '<', '>', '/', '?']
    #list_all = list_numbers + list_alpha_lowercase + list_alpha_uppercase + list_symbols
     
    Password = " "
    list_items = []
    if p["up"] == True :
         list_items.extend(list_alpha_uppercase) 
    if p["lo"] == True :
         list_items.extend(list_alpha_lowercase)
    if p["n"] == True : 
         list_items.extend(list_numbers )
    if p["sy"] == True : 
         list_items.extend(list_symbols)
    if p["up"] == p["lo"] == p["n"] ==p["sy"] == False :
         list_items.extend(list_numbers)

    print(list_items)
    for i in range(p['l']) : 
       #print("Boucle")
        """
        r = random.randint(1,5)
        if  r == 1 :
            Password = Password + str(random.choice(list_numbers)) 
        elif r == 2 :
            Password = Password + str(random.choice(list_alpha_lowercase)) 
        elif r == 3 :
            Password = Password + str(random.choice(list_alpha_uppercase))
        elif r == 4 :
            Password = Password + str(random.choice(list_symbols)) 
        else :  """
        Password = Password + str(random.choice(list_items))
       
            
         
    return Password 

# Main program 
#filep = open("pw.txt","a")
while True : 
    choice = display_menu()

    if choice == 1 :
       print("The password :" , G_default_pass())
       #type(G_default_pass()) 
       #filep.write(G_default_pass())
      # filep.newlines
        
    elif choice == 2 :
         print("The password :" , G_custom_pass())
    else :
        break

print("Programe ended")
#filep.close