str=input("Enter string: ")
sub_str=input("Enter character to find index: ")
count=0
#print (f"sub_str[0] = {sub_str[0]}")
for i in str:
	# print (i,count)
	count+=1
print(f"The number of characters in _{str}_ is {count}")
		

y=str.count(sub_str)
if y==0:
	print (f"number of occurences = {y}")
	print ("Not found")
elif y>=1:
	print (f"index is {str.find(sub_str)}")
	print (f"number of occurences = {y}")
	count=0
	for i in str:
		count+=1
		if i==sub_str[0]:
			x=count-1
			print("The index of the character is :",x)		
			break
#print(f"The number of occurences of the given character is {y}")	

# a=input("“Enter the word1:”")
# b=input("“enter the word2:”")
# print("“The no. of occurrence of this substring is:”",a.count(b))
# if(a.find(b)==-1):
#   print("“Not found”")
# else:
#   print(a.index(b))
