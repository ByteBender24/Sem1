x=int(input("Enter the start of the range: "))
y=int(input("Enter the end of the range: "))
count=0
x = x+1 if x==1 else x
for i in range(x,y+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:  
        count+=1
        print(i,end=" ")
print()
print (f"{count=}")             #f string




