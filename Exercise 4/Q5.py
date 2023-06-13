number = int(input("Enter the number to be checked: "))
y = number
rev=0
while number >= 10:
    x=number%10  
    rev=x+(rev*10)  
    number=number//10  
    # print ("The remainder is",x)  
    # print ("The quotient is",number)  
    if number < 10:
        rev=number+(rev*10)
        print ("reversed number =",rev)
if rev==y:
    print()
    print (rev,"is equal to",y)
    print ("The given number is a palindrome")
else:
    print ()
    print (rev,"is not equal to",y)
    print ("The given number is not a palindrome")


# #2
# number = int(input("Enter the number to be checked: "))   #Doubt
# y = number
# rev=0
# z=0
# x=str(0)
# while number >= 10:
#     listnumber = list(x)
#     x=number%10
#     rev=x+(rev*10)
#     number=number//10
#     # print ("The remainder is",x)
#     # print ("The quotient is",number)
#     x=str(x)
#     listnumber.append(x)
#     print (listnumber)
#     if number < 10:
#         rev=number+(rev*10)
#         listnumber.append(number)
#         print ("reversed number =",rev)
#         print (listnumber)
