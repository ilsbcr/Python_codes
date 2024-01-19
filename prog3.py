import random

choice = "y"

while choice.lower() == "y" :

    range_Top = int(input("Enter the top value of the range : "))
    range_Bottom = int(input("Enter the bottom value of the range : "))
    while True :
        if  range_Bottom > range_Top : 
            print("range_Bottom > range_Top ! Reenter ranges ")
            range_Top = int(input("Enter the top value of the range : "))
            range_Bottom = int(input("Enter the bottom value of the range : "))

        else : 
            break
    number = int(input("Enter a number :"))


    random_Number = random.randint(range_Bottom,range_Top)
    Propability = 1 / ((range_Top - range_Bottom )+1) 

    if(random_Number == number) :
        print("Correct ! , you are lucky , probalility of the correct number :" , Propability )

    else :
        print("NO ! probalility of the wrong number :" ,1 - Propability)


    print("Given number : ", number)
    print("Guessed number :",random_Number)

    choice = input("Do you want to continue y/n : ")
    if (choice.lower == "n") : 
        break

print("Game ended")