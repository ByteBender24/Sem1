a=int(input("Enter the coefficient of x^2 term: "))
b=int(input("Enter the coefficient of x term: "))
c=int(input("Enter the constant value: "))

d=(b**2)-4*a*c

if (d>0) :
	print ("The roots are real and unequal")
	y=d**(1/2)
	z1 = (-b+y)/(2*a)
	z2 = (-b-y)/(2*a)
	print ("The roots of the given quadratic equation is","\n",z1,"\n",z2)

elif (d==0) :
	print ("The roots are real and equal")
	z3=(-b/(2*a))
	print ("The root of the given quadratic equation is:","\n",z3)

elif (d<0) :
	print ("The roots are imaginary")
	y=d**(1/2)
	z3 = (-b+y)/(2*a)
	z4 = (-b-y)/(2*a)
	print ("The roots of the given quadratic equation is","\n",z3,"\n",z4)


