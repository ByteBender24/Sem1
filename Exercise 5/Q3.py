str=input("Enter string: ")
ch=input("Enter character to find index: ")
count=0
#print (f"ch[0] = {ch[0]}")
for i in str:
	#print (i,count)
	count+=1
print(f"The number of characters in _{str}_ is {count}")

count=0
for i in str:
	count+=1
	if i==ch:
		x=count-1
		break
y=0
for i in str:
	if i==ch:
		y=y+1
print(f"The number of occurences of the given character is {y}")	
print(f"The index of the character is : {x}")
