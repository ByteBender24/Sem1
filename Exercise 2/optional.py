# #1
# speed_of_light = 3*(10**8)
# seconds_in_a_year = 365*24*60*60
# Light_year = speed_of_light * seconds_in_a_year
# print (Light_year)

# #2
# old = int(input("how many oldies: "))
# new = int(input("how many new videos: "))
# Total_cost = old*2 + new*2
# print (f"${Total_cost}")

# #3
# hourlywage = int(input("enter the hourly wage: "))
# regularhr  = int(input("enter how many total regular hours: "))
# overtimehr = int(input("enter how much overtime hours: "))
# overtime_pay  = overtimehr * 1.5 * hourlywage
# total_weekly_pay = hourlywage*regularhr + overtime_pay
# print (f"₹{total_weekly_pay}")

# #4
# letter = input('Please enter an upper-case or lower-case letter: ')
# letter_encoded = ord(letter)
# print(f'The Unicode encoding for {letter} is {letter_encoded}')

#5
xr=eval(input("Real part of first Number: "))
xi=eval(input("Imaginary part of first Number: "))
yr=eval(input("Real part of second Number: "))
yi=eval(input("Imaginary part of second Number: "))
x=complex(xr,xi)
y=complex(yr,yi)
print (x)
print (y)
print (f"add={x+y}")
print (f"sub={x-y}")
print (f"multi={x*y}")