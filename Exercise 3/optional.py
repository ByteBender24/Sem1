# #1
# rl_age = int(input("Enter the age of dog: "))
# if rl_age == 1:
#     print ("If it was not a dog, but a human being, it is 14 years old")
# elif rl_age == 2:
#     print ("If it was not a dog, but a human being, it is 22 years old")
# else:
#     x=22+(5*(rl_age-2))
#     print (f"If it was not a dog, but a human being, it is {x} years old")


# #2
# rain_prob = input("Will it rain tomorrow? Yes or No : ")
# if rain_prob == "Yes":
#     print ("It will rain")
#     print ("Tidy up the cellar")
#     print ("Paint the walls")
#     time_left = input("Some time left? Yes or No: ")
#     if time_left == "Yes":
#         print ("Do tax declaration")
#         print ("Go to the cinema in the evening")
#     elif time_left=="No":
#         print ("Continue with your job")
# elif rain_prob == "No":
#     print ("Go swimming")
#     print ("Go to the cinema in the evening")

# #3
# number = int(input("Enter a number: "))
# if number%2 == 0:
#     print (f"{number} is even")
#     if number%4 == 0:
#         print (f"{number} is divisible by 4")
#     else:
#         print (f"{number} is not divisible by 4")
# else:
#     print (f"{number} is odd")
#     if number%3 == 0:
#         print (f"{number} is divisible by 3")
#     else:
#         print (f"{number} is not divisible by 3")

# #4
# str1 = input("Enter string 1: ").lower()
# str2 = input("Enter string 2: ").lower()
# str3 = input("Enter string 3: ").lower()

# print ("Given strings in dictionary order:")

# if str1<str2 and str1<str3:
#     print (str1)
#     if str2<str3:
#         print (str2)
#         print (str3)
#     else:
#         print (str3)
#         print (str2)
# elif str2<str1 and str2<str3:
#     print (str2)
#     if str1<str3:
#         print (str1)
#         print (str3)
#     else:
#         print (str3)
#         print (str1)
# elif str3<str2 and str3<str1:
#     print (str3)
#     if str1<str2:
#         print (str1)
#         print (str2)
#     else:
#         print (str2)
#         print (str1)

#5
x=int(input("Enter a number: "))
n=int(input("Enter number of terms: "))
if n==1:
    y=1+x
elif n==2:
    y=1+(x/n)
elif n==3:
    y=1+(x**n)
elif 3<n<1:
    y=1+n*x
print (y)