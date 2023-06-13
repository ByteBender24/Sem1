# Write a python program to remove duplicates from tuple.

test_list = (4, 5, 4, 5, 6, 6, 6)

# method 1: (forming a new tuple )
unique = []
for i in test_list:
    if i not in unique:
        unique.append(i)

print (tuple(unique))

#method 2: (from the old tuple)
test_list_list=list(test_list)
unique = []

for i in test_list:
    if i not in unique:
        unique.append(i)
        test_list_list.remove(i)    #there is a small mistake #oa
print (tuple(test_list_list))