a=int(input("Enter the subject one marks = "))
b=int(input("Enter the subject two marks = "))
c=int(input("Enter the subject three marks = "))
d=int(input("Enter the subject four marks = "))
e=int(input("Enter the subject five marks = "))

#Percentage of the total marks obtained :
x=((a+b+c+d+e)/500)*100

if 100>=x>=90 :
	print ("\n","Congratulations. You have passed with Distinction.")
elif 80<=x<90 :
	print ("\n","Congratulations. You have passed with First class.")
elif 70<=x<80 :
	print ("\n","Congratulations. You have passed with Second class.")
elif 60<=x<70 :
	print ("\n","Congratulations. You have passed with Third class.")
elif x<60 :
	print ("\nSorry to say. You have Failed. Better luck next time.") #Here I have removed the comma to get the indentation right
else :
	print ("\n","Your input is wrong. Please check your inputs.")
