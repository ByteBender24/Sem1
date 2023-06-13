#not by simultaneous assignment
#By assigning a temporary variable

x = int(input("Enter x"))
y = int(input("Enter y"))
a=x
x=y
y=a
print (x,y)
