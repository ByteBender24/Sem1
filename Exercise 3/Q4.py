a=int(input("Enter subject one marks "))
b=int(input("Enter subject two marks "))
c=int(input("Enter subject three marks "))

x=(a+b+c)/3
if (90<=x<=100) :
	print("\nYou have secured Grade A.")
elif (80<=x<=89) :
	print("\nYou have secured Grade B.")
elif (70<=x<=79) :
	print("\nYou have secured Grade C.")
elif (69<=x<=60) :
	print("\nYou have secured Grade D.")
elif (0<=x<=59) :
	print ("\nSorry. You have failed. You secured Grade F.")

