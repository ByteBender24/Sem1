# x=int(input("Enter a number to find GCD"))     #Doubt
# y=int(input("Enter another to find GCD"))

# temp = 0

# if x > y:
#     temp = y
# else:
#     temp = x

# # for i in range(1, temp + 1):
# #     if (x%i == 0) and (y%i == 0):
# #         gcd = i


# def gcd(a,b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a%b)

# print(gcd(x,y))


a=int(input("Enter a number to find GCD"))     #Doubt
b=int(input("Enter another to find GCD"))

# temp = 0

# if y>x:
#     x,y=y,x
# for i in range(1,y+1):
#     x = x//y

while b:
    a, b = b, a % b
print (a)
