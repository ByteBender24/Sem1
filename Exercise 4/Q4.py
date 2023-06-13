Dividend = int(input("Enter the dividend value: "))
Divisor = int(input("Enter the divisor value: "))
count = 0
while Dividend > Divisor:
    Dividend = Dividend - Divisor
    #print ("Check=",Dividend) 
    count += 1
y=Dividend
x=count
print ("The quotient is",x)
print ("The remainder is",y)
