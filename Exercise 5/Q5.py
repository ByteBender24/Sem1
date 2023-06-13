str=input("Enter the string: ")
if str == str[::-1]:
	print (f"{str} = {str[::-1]}")
	print (f"{str} is a palindrome")
else:
	print (f"{str} is not a palindrome")
