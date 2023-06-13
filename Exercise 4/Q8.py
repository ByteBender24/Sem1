# v=int(input("Enter the voltage value: "))

# if v==5:
#     print ("ACTIVE")
# elif 0<v<5:
#     print ("CUTOFF")
#     i=v
#     while i!=5 and i<=5:
#         i=int(input("Enter the voltage value: "))
#     print ("BREAKDOWN")
# elif v>5:
#     print ("BREAKDOWN")

v=5
while v!=0:
    v=int(input("Enter the voltage value: "))
    if 0<v<5:
        print ("CUTOFF")
        break
    elif v>5:
        break 
    #as the code terminates when we enter breakdown voltage