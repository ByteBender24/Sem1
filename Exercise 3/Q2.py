a=int(input("Enter the length of first side = "))
b=int(input("Enter the length of second side = "))
c=int(input("Enter the length of third side = "))

if(a==b==c):
	print ("The triangle is equilateral.")
elif(a==b):
	print ("The triangle is isosceles.")
elif(b==c):
	print ("The triangle is isosceles.")
elif(a==c):
	print ("The triangle is isosceles.")
else:
	print ("The traingle is scalene.")

#This is one way of code, I can make it shorter by using "or"
'''
a=int(input("Enter the length of first side = "))
b=int(input("Enter the length of second side = "))
c=int(input("Enter the length of third side = "))

if(a==b==c):
	print ("The triangle is equilateral.")
elif (a==b) or (b==c) or (a==c):
	print ("The triangle is isosceles.")
else:
	print ("The triangle is scalene.")
'''