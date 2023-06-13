f1 = open('SSN exercises\Exercise 10\q3.txt','r')
f2 = open('SSN exercises\Exercise 10\q3copied.txt','w')

print (f1.tell())
print (f2.tell())
lines = f1.readlines()
print (lines)
for line in lines:
    if line.startswith("#") == True:
        continue
    else:
        f2.write(line)
    # f2.write("\n")

print (f1.tell())
print (f2.tell())


f1.close()
f2.close()

            