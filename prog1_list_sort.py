#sort a list 

def func1 (l):
    print("func1 ")
    l.sort()
    return l

def func2 (l) :
    print("func2 ")
    l.sort(reverse = True)
    return l

print("This program is for sort a list")
nb = int(input("what is the number of Items : "))

while nb < 0:
    nb = int(input("Enter a value greater than 0: "))

list = []

print("Enter the list items (separated by spaces):")
items_str = input()
items = items_str.split(" ")

for i in range(nb):
    item = items[i]  # Access items from the input list
    #print("Item", i + 1, ":", item)  # Print item with index
    list.append(item)

print("The list :", list)

print("Choose one option below :")
print("1 - Ascending sort")
print("2 - Descending sort")
choice  = input()

if choice == "1":
   list_ADsorted = func1(list)
elif choice == "2":
   list_ADsorted = func2(list)

print("List sorted : " , list_ADsorted)
