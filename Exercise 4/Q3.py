#1
# i=10
# while i<100:
#     if (i%3==0) or (i%4==0):
#         if (i%3==0):
#             print ("divisible by 3 =",i)
#         else:
#             print ("divisible by 4 =",i)
#     i=i+1

i=10
print("numbers divisible by 3 or 4 before 100: ")
while i<100:
    if (i%3==0) or (i%4==0):
        print(i,end=" ")
    i=i+1 
