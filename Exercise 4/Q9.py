# n=int(input("Enter the number to find the square root: "))
# x=int(input("Enter a random number: "))

# #tolerance level = L = 0.0001
# a=abs(n-x)
# while a<1:
#     root = (1/2) * (x + (n / x))
#     a+=0.0001
#     print (root)
# print ("The square root of the given number is",root)


# n=int(input("Enter a random number"))
# x=int(input("Enter base value"))                #Doubt
# approx_root = n
# for i in range(x):
#     betterapprox = 0.5 * (approx_root + n/approx_root)
#     approx_root = betterapprox
# print(betterapprox)

def newtonsqrt(n):
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while better!=approx:
        approx=better
        better=0.5*(approx+n/approx)
    return approx
print(newtonsqrt(9))