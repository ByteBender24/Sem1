# 1. Write a python program to display the number in words [Tuple].
# Eg. 123 O/p: ("one", "two”, “three”)

num = int(input("enter the number: "))

num_name = ('zero','one','two','three','four','five','six','seven','eight','nine','ten')
# list = []
# for i in str(num):
#     list.append(num_name[int(i)])

list = [num_name[int(d)] for d in str(num)]    

print (tuple(list))
