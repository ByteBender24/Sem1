import random
s=0
a = int(input("Input of how many random numbers: "))

for i in range(1,a+1):
    t=random.randint(1,1000)
    s=s+t
print(s)