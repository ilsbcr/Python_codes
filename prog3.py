import random

choice = "y"

while choice.lower() == "y" :

    range_Top = int(input("Enter the top value of the range : "))
    range_Bottom = int(input("Enter the bottom value of the range : "))
    number = int(input("Enter a number :"))


    random_Number = random.randint(range_Bottom,range_Top)

    if(random_Number == number) :
        print("Correct ! , you are lucky , probalility of the correct number :" , 1 / ((range_Bottom +  range_Top )-1) )

    else :
        print("NO !")


    print("Given number : ", number)
    print("Guessed number :",random_Number)

    choice = input("Do you want to continue y/n : ")
    if (choice.lower == "n") : 
        break

print("Game ended")