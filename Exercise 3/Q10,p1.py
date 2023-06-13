#Doubt

# a=int(input("Enter the year to check whether it's a leap year of not = "))

# if (a%100==0):
# 	if (a%4==0):
# 		print ("The year is not a leap year")

# 	elif (a%400==0):
# 		print ("The year is a leap year")
# else :
# 	print ("U are wrong")

x=int(input("enter a year:"))
if(x%4==0):
  if(x%400==0) and (x%100==0):
    print("It is a leap year")
else:
    print("It is not a leap year")
