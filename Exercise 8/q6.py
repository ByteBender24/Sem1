# Given a list, find frequency of each element and save it as list of tuple
# [(number, frequency)].
# Input : test_list = [4, 5, 4, 5, 6, 6, 5]
# Output : [(4, 2), (5, 3), (6, 2)]
# Input : test_list = [4, 5, 4, 5, 6, 6, 6]
# Output : [(4, 2), (5, 3), (6, 3)] 

test_list = [4, 5, 4, 5, 6, 6, 6]
unique = []
for i in test_list:
    if i not in unique:
        unique.append(i)

print (unique)
freq=[]
for i in unique:
    count=0
    # freq_single=[i,count]       why does not this code work?
    for j in test_list:
        if j == i:
            count+=1
    freq_single=[i,count]         # but here it works well? #qtp
    freq.append(tuple(freq_single))

print (freq)