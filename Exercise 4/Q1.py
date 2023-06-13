#1:
base = int(input("Enter the base number: "))
power = int(input("Enter the power to be raised: "))

i=1
a=1
while i<=power:                                                                     #think for power zero case - WHY & HOW
    a=base*a
    #print("Check=",base,"raised to the power of",i,"is",a)
    i=i+1
print (f"\n{base} raised to the power of {power} is {a}.")


#2:
# base = int(input("Enter the base number: "))
# power = int(input("Enter the power to be raised: "))

# i=1
# a=base
# while i<=(power-1):
#     print("Check=",a,"raised to the power of",i,"is",base)
#     base=base*a
#     i=i+1
# print ("\nThe exponentiation answer for the given numbers is:",base)