#sort a list 

print("This program is for sort a list")
nb = int(input("what is the number of Items : "))

while nb < 0:
    nb = int(input("Enter a value greater than 0: "))

list = []

print("Enter the list items (separated by spaces):")
items_str = input()
items = items_str.split()

for i in range(nb):
    item = items[i]  # Access items from the input list
    print("Item", i + 1, ":", item)  # Print item with index
    list.append(item)

print("Final list:", list)