#Fibonacci:

# def Fib(n):
#     f1=0
#     f2=1
#     print (f1,f2,end=" ")
#     for i in range(n-2):
#         f3=f1+f2
#         f1=f2
#         f2=f3
#         print (f3,end=" ")

# Fib(10)

# def fibonacci(n):
#     if(n <= 1):
#         return n
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))
# n = int(input("Enter number of terms:"))
# print("Fibonacci sequence:")
# for i in range(n):
#     print(fibonacci(i))

# def Fact(n):
#     if n<=1:
#         return 1
#     else:
#         x = n * Fact(n-1)
#         return x 

# print(Fact(5))

# Power:
# def power(n,p):
#     if  p==0:
#         return 1
#     elif p==1:
#         return n
#     else:
#         n=n
#         x=p-1
#         return n*power(n,p-1)

# print(power(10,3))

#write a recursive function that given an input n sums all non-negative integers up to n:

def sum_of_positive(n):
    if n==0:
        return 0
    else:
        print (f"n={n}")
        return n+(sum_of_positive(n-1))

print (sum_of_positive(4))

#Write a function that takes two inputs n and m and outputs the number of unique paths from th etop left corner to bottom right corner of a nxm grid. 
#Constrainsts: you can only move down or right 1 unit at a time.

def grid(n,m):
    if n==1 or m==1:
        return 1
    else:
         return grid(n,m-1) + grid(n-1,m)

print (grid (2,2),grid (5,5),grid (5,4),grid (2,3))

#Write a function that counts the number of ways you can partition n objects using parts up to m: (m>0)
#https://youtu.be/ngCos392W4w

#write a function to solve GCD using recursion

def GCD(a,b):
    if b==0:
        return a
    else:
       return GCD (b,a%b)

print (GCD(4,16))