x=int(input("Enter the number to be checked: "))
a=x
i=1
while x>=10:
    x=x/10
    i=i+1
    # print (i)
print ("number of digits=",i)

#another method (with use of built-in function):
#print(len(str(x)))


x=a
b=x
sum = 0
while x>=10 :
    a=x%10
    x=x//10
    sum = sum + a**i
    # print("remainder=",a)
    # print("quotient=",x)
    if x<10:
        sum = sum + x**i
        print (sum)
        
if sum == b:
    print ("The given number is an ARMSTRONG NUMBER")
else:
    print ("The given number is NOT AN ARMSTRONG NUMBER")



