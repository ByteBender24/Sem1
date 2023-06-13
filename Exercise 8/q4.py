# Write a Python program to create a list of tuples having first element as the
# number and second element as the cube of the number.


num_list = []
new_num_list = []
while True:
    choice = int(input('''Enter your choice.
    Enter 1 to enter numbers.
    Enter 2 to stop
    '''))

    if choice == 2:
        break

    num = int(input("Enter number : "))
    num_list.append(num)

for i in num_list:
    new_num_list.append(tuple([i,i**3]))

print (new_num_list)