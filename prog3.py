import random

number = int(input("Enter a number :"))
random_number = random.randint(1,10)

if(random_number == number) :
    print("Correct !")

else :
    print("NOO")

    print("Given number : ", number)
    print("Guessed number :",random_number)