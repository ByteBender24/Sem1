#I have used the "eval" function to get input for both float and integer
x=eval(input("Enter the number to get the absolute value of it = "))

if (x>=0) :
	if (x>0) :
		print ("\n","The given number is a positive number.""\n","Hence the absolute value of the given number is",x)
	if (x==0) :
		print ("\n","The given number is Zero.""\n","Hence the absolute value of the given number is",x)

elif (x<0) :
	y= -x
	print ("\n","The given number is a negative number.""\n","Hence the absolute value of the given number is",y)

