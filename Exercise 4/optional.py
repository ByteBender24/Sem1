# #1
# no_yr=int(input("Enter the number of years: "))
# i=1
# fee = 10000
# while i<=no_yr:
#     fee=fee+(fee)*0.05
#     i=i+1
#     # print ("check",i,fee)
# print (f"Tuition in {i} years : ${round(fee)}")

# i=0
# while i<4:
#     fee = fee + (fee)*0.05
#     i=i+1
# print (f"Total cost of 4 years' worth of tuition starting 10 years from now: ${round(fee)}")


#2
no_students = int(input("Enter the number of students: "))
i=1
temp = 0
temp2 = 0
temp3 = 0
while i<=no_students:
    mark = int(input(f"Enter mark of student{i}: "))
    if mark>temp:
        temp = mark
    if temp2>temp:
        temp2 = temp
    temp2 = temp
    i=i+1

print ("first mark",temp)
print ("second mark",temp3)

#3
# decimal = int(input("Enter the decimal number: "))
# print ("Convert decimal to binary:")
# while True:
#     quotient = decimal%2
#     decimal = decimal//2
#     count = count + "1"
#     if quotient == 1:
#         str(quotient)
    
    
        
# for i in "Go Spot Go":
#     print ( i )
# print () 
# fruit = "apple"
# for idx in range (len(fruit)-1,-1,-1):
#     print (fruit[idx],end="")
# for idx in range (0,len(fruit),-1):
#     print (fruit[idx],end=" ")


# n = int(input("Enter the number of students: "))
# first_high = second_high = float("-inf")
# for i in range(n):
#     score = float(input("Enter student #%d's score: " % (i + 1)))
#     if score > first_high:
#         second_high = first_high
#         first_high = score
#     elif score > second_high and score < first_high:
#         second_high = score

# print("The highest score is:", first_high)
# print("The second highest score is:", second_high)
 

    

