#Create two lists storing the names of the persons in L1 and age of the corresponding
# person in L2 . Write a Python program to convert them into a dictionary in a way that
# item from list1 is the key and item from list2 is the value. 

L1 = []
L2 = []

while True:
    choice = int(input('''Enter your choice.
    Enter 1 to enter data.
    Enter 2 to stop
    '''))

    if choice == 2:
        break

    name = input("Enter name of the person: ").capitalize()
    age = int(input(f"Enter the age of {name}: "))
    L1.append(name)
    L2.append(age)

print (L1)
print (L2)

data = dict(zip(L1,L2))
print (data)