a =int(input("enter the a value "))
b =int(input("enter the b value "))
c =int(input("enter the c value "))

x=(b**2)-4*a*c
y=x**(1/2)
z1 = (-b+y)/(2*a)
z2 = (-b-y)/(2*a)

print ("The roots of the given quadratic equation are:","\n",z1,"\n",z2)


##also can use cmath and if conditions also:

# import cmath
# import math

# a=int(input("Enter the a value: "))
# b=int(input("Enter the b value: "))
# c=int(input("Enter the c value: "))

# x=(-b+(cmath.sqrt((b**2)-(4*a*c))))/(2*a)
# y=(-b-(cmath.sqrt((b**2)-(4*a*c))))/(2*a)

# print("The values of the roots are: \n", x,"\n",y)