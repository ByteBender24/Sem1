#Fibonacci Series = 0 1 1 2 3 5 8 13 21....
N=int(input("For how many numbers should the series continue: "))
print("\nFibonacci series: ")
f1=0
f2=1
print(f1,end=" ")
print(f2,end=" ")
for i in range(2,N):
    sum=f1+f2
    f1=f2
    f2=sum
    if i==N-1:
        print(sum,end="...")
        break
    print(sum,end=" ")


# #Another method using functions:   #Doubt
# def fibonacci(n): 
#     a = 0
#     b = 1
#     if n < 0: 
#         print("Incorrect input") 
#     elif n == 0: 
#         return a 
#     elif n == 1: 
#         return b 
#     else: 
#         for i in range(2,n): 
#             c = a + b 
#             a = b 
#             b = c 
#         return c

# #test
# print(fibonacci(9))
