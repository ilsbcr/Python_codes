#count number of vowels in a string

word = input("Enter a word to count it's vowels :")

vowels_counter = 0 
vowels = ['a','u','e','i','o']

for lettre in word :
    #print(lettre)
    if lettre.lower() in vowels :
       # print("vowel : " + lettre )
        vowels_counter += 1

print("The number of vowels in " + word + " is : " + str(vowels_counter))

