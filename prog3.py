import random

range_Top = int(input("Enter the top value of the range : "))
range_Bottom = int(input("Enter the bottom value of the range : "))
number = int(input("Enter a number :"))


random_Number = random.randint(range_Bottom,range_Top)

if(random_Number == number) :
    print("Correct !")

else :
    print("NOO")


print("Given number : ", number)
print("Guessed number :",random_Number)