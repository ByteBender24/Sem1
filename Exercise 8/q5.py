# Given list of tuples, remove all the tuples with length K.
# Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2
# Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
# Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 3
# Output : [(4, 5), (4, ), (1, ), (3, 4, 6, 7)]


test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

K = int(input("Enter the tuple length: "))

for i in test_list:
    if len(i) == K:
        test_list.remove(i)

print (test_list)