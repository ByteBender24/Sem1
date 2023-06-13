# print("#a")
# # x=int(input("Enter the number of rows: "))                    1
# # for i in range (x+1):                                         1 2
# #     for j in range (1,i+1):                                   1 2 3
# #         print(j,end=" ")                                      1 2 3 4
# #         if j==i:
# #             print()

# x=int(input("Enter the number of rows: "))                    #same as before
# for i in range (x+1):
#     for j in range (i):
#         print(j+1,end=" ") 
#         if j==i-1:
#             print()


# # x=int(input("Enter the number of rows: "))
# # for i in range(x+1):                                              1
# #     for j in range (i,0,-1):                                      2 1
# #         print(j,end=" ")                                          3 2 1
# #         if j==1:                                                  4 3 2 1
# #             print() 

# print("#b")
# x=int(input("Enter the number of rows: "))
# for i in range(x):
#     print(" "*(x-i-1),end="")      #without this line, the output looks like previous one with *
#     for j in range(i+1):
#         print("*",end=" ")
#         if j==i:
#             print()

# print("#c")
# x=int(input("Enter the number of rows: "))
# for i in range(x):
#     print(" "*(x-(i+1)),end="")
#     for j in range (i+1):
#         print("a",end=" ")
#         if j==i:
#             print()



# x=int(input("“How many starlines to print?”"))
# y=int(x)
# for i in range(1,y+1):
#   print((y-i)* " ",(2*i-1)* "*")

# from math import factorial
# n=5
# for i in range(n):
#     for j in range(n-i+1): 
#         print(end=' ')
# for j in range(i+1):                                 
#     print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
#     print()

# x=int(input("Enter the number of rows: "))
# for i in range(1,x+1):
#     print (" "*(x-i),end="")
#     for j in range (1,i+1):
#         print (j,end=" ")
#         if j==i:
#             print()


# x=int(input("Enter the number of rows: "))
# for i in range(x):
#     print(" "*(x-(i+1)),end="")
#     for j in range (i+1):
#         print("a",end=" ")
#         if j==i:
#             print()

x=int(input("Enter the number of rows: "))
for i in range(1,x+1):
    print (" "*(x-i),end="")
    C=1
    for j in range (1,i+1):
        print(C,end=' ')
        C = C * (i-j)//j
    print()

