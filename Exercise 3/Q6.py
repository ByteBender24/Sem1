a=int(input("Enter the current month's reading. "))
b=int(input("Enter the previous month's reading. "))

#I have used abs() function here to get a positive difference in reading.

x=abs(a-b)

if x>1000 :
	y = int(x*5)
	print("The electricity bill for your household is Rs.",y)
elif 500<x<1000 :
	y = int(x*3)
	print("The electricity bill for your household is Rs.",y)
elif x<500 :
	y = int(x*1.5)
	print("The electricity bill for your household is Rs.",y)
