#a) 1,3,9,27,81,243...

x=int(input("For how many numbers you want for the series:\n     1,3,9,27,81,243...\nEnter here: ")) 
y=1
print(y,end=",")
for i in range(x):
    y=y*3
    i=i+1
    if i==x-1:
        print(f"{y}",end="...")
        break
    print (f"{y}",end=",")


#c) 1,8,27,64...
x= int(input("\nFor how many numbers you want for the series\n      1,8,27,64...\nEnter here: "))

for i in range(1,x+1):
    if i==x:
        print(i**3,end="...")
        break
    print(i**3,end=",")
    i=i+1
    
#b) 