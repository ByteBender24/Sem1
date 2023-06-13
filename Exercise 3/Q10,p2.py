# a=int(input("Enter the year: "))

# if ((a%4==0) and (a%100==0) and (a%400==0)) :
# 	print ("The given year",a,"is a leap year.")
# else :
# 	print ("The given year",a,"is not a leap year.")


year = int(input('Enter year : '))
 
if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
    print(year, "is a leap year.")
else :
    print(year, "is not a leap year.")