#1
number = int(input("Enter the number to be tested: "))
sum=0
y=number
while y>0:
    x=y%10
    print ("check = The remainder is",x)
    y=y//10
    print ("check = The quotient is",y)
    sum=sum+x
    
print ("\nThe sum of the digits of the given number is",sum,"\n")

if sum>=10:                                 
    y=sum
    while y>=10:
        x=y%10
        print ("check = The remainder is",x)
        y=y//10
        print ("check = The quotient is",y)
        sum=x+y
        print(sum)
        if sum>=10:                                       #
            y=sum
            while y>=10:
                x=y%10
                print ("check = The remainder is",x)
                y=y//10
                print ("check = The quotient is",y)
                sum=x+y
        print ("\nThe sum of the digits of the returned sum value is",sum,"\n")
else:
    print("")


# 2
# def sumofDigits(y):
#     sum = 0
#     while y>0:
#         x=y%10
#         # print ("check = The remainder is",x)
#         y=y//10
#         # print ("check = The quotient is",y)
#         sum=sum+x
#     return sum

# number = int(input("Enter the number to be tested: "))

# while True:
#     number = sumofDigits(number)
#     if number < 10:
#         print ("\nThe sum of the digits of the given number is",number,"\n")
#         break


#decimal point additions
