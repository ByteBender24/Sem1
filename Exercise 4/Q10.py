#using For loop
y=int(input("Enter the number you want to have multiplication table for = "))
x=int(input("Multiplication table for how many times? = "))
for i in range (x+1):
    a=y*i
    print (y,"x",i,"=",a)


#using While loop
y=int(input("Enter the number you want to have multiplication table for = "))
x=int(input("Multiplication table for how many times? = "))

i=0
while i<=x:
    a=y*i
    print(f"{y} x {i} = {a}")
    i=i+1

#print("{} x {} = {}".format(y,i,a))       #format of
#print (y,"x",i,"=",a)                      #f string