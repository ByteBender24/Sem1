S=int(input("Enter the salary amount of the employee. "))
G=str(input("Enter the gender of the employee.Enter 'Female' or 'Male' "))

if (G == "Female") :
	if (S<=10000) :
		x = (0.15*S)+(0.02*S)+S
	elif (S>10000) :
		x = (0.15*S)+S
	print (x)
else :
	if (S<=10000) :
		x = (0.05*S)+(0.02*S)+S
	elif (S>10000)  :
		x = (0.05*S)+S
	print (x)

#I can also use the "and" relation and solved this one.