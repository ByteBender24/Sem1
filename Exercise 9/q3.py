# Write a Python program to combine two dictionary adding values for common keys.
d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
# a. Infer the output of the new dictionary
# b. Display only the keys of the new dictionary
# c. Display only the values
# d. Display the key_value pair 

for key1 in d1.keys():
    if key1 in d2.keys():
        d1[key1] = d1[key1] + d2[key1]
        d2.pop(key1)
    
for key2 in d2.keys():
    d1[key2]=d2[key2]

# a
print ("dictionaries")
print (d1)

# b
print ("keys")
print (list(d1.keys()))

#c
print ("key-value pairs")
for i in d1.items():
    print (i)

values = []
print ("values")
for x,y in d1.items():
    values.append(y)

print (values)
    




