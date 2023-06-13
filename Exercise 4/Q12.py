#FACTORIAL OF A NUMBER:
#Using for loop
x=int(input("Enter the number to find the factorial of: "))
y=1
for i in range(x):
    i=i+1
    y=y*i
    print (f"{i}!={y}")
print (f"The factorial of {x} is {y}.")

#Using while loop:
# x=int(input("Enter the number to find the factorial of: "))
# y=1
# i=0
# while i<=x:
#     i=i+1
#     y=y*i
#     print (f"{i}!={y}")
# print (f"The factorial of {x} is {y}.")

    