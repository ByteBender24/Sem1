str=input("Enter the string: ")
upper = 0
lower = 0
spl = 0
num = 0
for i in str:
    if i.isupper()==1:
        print (f"upper {i}")
        upper+=1
    elif i.islower()==True:
        print(f"lower {i}")
        lower +=1
    elif i in '1234567890':
        print(f"number {i}")
        num +=1
    else: 
        
        print (f"spl {i}")
        spl +=1

print (f"No.of uppercase : {upper}")
print (f"No.of lowercase : {lower}")
print (f"No.of numbers : {num}")
print (f"No.of special characters : {spl}")

