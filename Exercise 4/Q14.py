#a) 1+x^2/2 + x^3/3 +.........x^n/n
x=int(input("Enter the base value of this series= "))
n=int(input("Enter till how many numbers= "))
sum=1
for i in range(2,n+1):
    z=(x**i)/i
    # print(f"z={z}")
    sum=sum+z
    # print(f"sum={sum}")
    # print("i=",i)
    i=i+1
print (f"\nThe sum of the series 1 + {x}^2/2 + {x}^3/3 +........{x}^{n}/{n} is {sum}")

# b)-x + x^2 - x^3 + x^4 + ....
x=int(input("Enter the base value of this series= "))
n=int(input("Enter till how many numbers= "))
sum=0
for i in range(1,n+1):
    if i%2!=0: #odd
        y=-(x**i)
        #print(f"odd y={y}")
    elif i%2==0:
        y=(x**i)
        #print(f"even y={y}")
    sum=sum+y
    #print("Sum=",sum)
print("The final sum is",sum)



#or :use this method:
x=int(input("Enter the base value of this series= "))
n=int(input("Enter till how many numbers= "))
sum=0

for i in range(1,n+1):
    y= ((-1)**i)*(x**i)
    #print (y)
    sum=sum+y
    #print (sum)
a=((-1)**n)*x
if n>4:
    print(f"The sum of the series -{x} + {x}^2 - {x}^3 + {x}^4....{a}^{n} is : ",sum)
else:
    print(f"The sum of the series is : ",sum)




