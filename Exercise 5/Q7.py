# #Lexicographical order in a string:
# str = list((input("Enter a string: ")))
# # for i in range(len(str)-1):
# #   for j in range (i): 
# #   if str[i]>str[i+1]:
# #         str[i],str[i+1]=str[i+1],str[i]
# str.sort()
# print(str)
# strings = "HelloThere"
# for i in range(len(strings)):
#     for j in range(i + 1, len(strings)):
#         if strings[i] > strings[j]:
#             strings[i], strings[j] = strings[j], strings[i]
#     print (strings)

str=list(input("Enter a string: "))
for i in range(len(str)):
    for j in range(i+1,len(str)):
        if str[i]>str[j]:
            str[i],str[j]=str[j],str[i]
    print(str[i],end="")
        # print ("check1",str)
    # print("check2",str)
# print ("checkfinal",str)
# print ("sorted string:",end="")
# for i in str:
#     print (i,end="")

# str=input("Enter a string: ")
# str2=""
# for i in range(len(str)):
#     for j in range(i+1,len(str)):