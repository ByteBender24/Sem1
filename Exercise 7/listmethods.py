

print("-----append-----")
my_list = [3, 8, 1, 6, 0, 8, 4]
my_list.append(5)
print(my_list)
print("\n\n\n\n\n\n")



# extend one list with another
# language list
language = ['French', 'English', 'German']
# another list of language
language1 = ['Spanish', 'Portuguese']
language.extend(language1)
# Extended List
print('Language List: ', language)



print("\n\n\n\n\n\n")
#my_list.extend(language1)
#print(my_list)


#if use append with list, other list will be considered as as single element and appended
#but if use extend, the elements are considered as individual elements.
l1=[1,2,3]
print(my_list)
my_list.extend(l1)
print(my_list)
my_list.append(l1)
print(my_list)


print("\n\n\n\n\n\n")


#to pop out elements or sub list (removes and returns)
print(my_list)
print(my_list.pop(3))
print(my_list.pop(-1))
print(my_list)
#[3, 8, 1, 0, 8, 4, 5]
#elements will be completely removed
print("\n\n\n\n\n\n")
#


#for removing elements in the list
#first occuerence of the element will be removed
print(my_list)
my_list.remove(1)
print(my_list)
my_list.remove(8)
print(my_list)



print("\n\n\n\n\n\nindex")
#returns the index value of the first occurance of the value
print(my_list)
print("index of 3 is =",my_list.index(3))



print("\n\n\n\n\n\n")
#to sort elements in the list
print(my_list)
my_list.sort()
print("sorted list",my_list)






print("\n\n\n\n\n\n")


#to reverse the elements in the list
print(my_list)
my_list.reverse()
print("reversed list",my_list)
my_list2=[6,4,2,9]
my_list2.reverse()
print(my_list2)


print("\n\n\n\n\n\nInsert")
#insert element at defined position
print(my_list)
my_list.insert(2,100)
print(my_list)
my_list.insert(6,100)
print(my_list)


print("\n\n\n\n\n\nCount")
#count() method counts how many times an element has occurred in a list and returns it.
print(my_list)
print(my_list.count(100))
print(my_list.count(4))


print("\n\n\n\n\n\nCopy")
#copy makes copy of another list; does not modify orginal list
print(my_list)
l2=my_list.copy()
print(l2)
l2.append(12)
print(l2)
print(my_list)


print("\n\n\n\n\n\nmatrix")
m=[[1,3],[1,4],[4,5]]
print(m)
for i in range(3):
  for j in range(2):
    print(m[i][j],end=" ")
  print()


print("\n\n\n\n\n\n")


rows,cols=3,2
l = []
for i in range(rows):
    l.append([5] * cols)
print(l)
    
print("\n\n\n\n\n\n")


l=[]
rows,cols=3,2
for i1 in range(rows):
    l.append([0]*cols)
    for i2 in range(cols):
        l[i1][i2]=int(input("Enter number[{}][{}]: ".format(i1,i2)))
               
for i1 in range(rows):
    for i2 in range(cols):
        print ( l[i1][i2],end=' ')
    print()
      
print("\n\n\n\n\n\nall()")
#all() returns 
#True - If all elements are true or empty list
#False - If any element is false
l = [1, 3, 4, 0]
print(all(l))
l = [1, 3, 4, 1]
print(all(l))
l = []
print(all(l))


print("\n\n\n\n\n\nany()")
#any() returns 
#True - If any element is true 
#False - If all elements are false or empty
l = [1, 3, 4, 0]
print(any(l))
l = [0, False]
print(any(l))
l = [0, False, 5]
print(any(l))
l = []
print(any(l))


print("\n\n\n\n\n\nenumerate()")
#enumerate:
# printing the tuples in object directly (ie, index and value)
#enumerate(iterable, start)
#start is optional, if it is not given, taken as 0
l1 = ["eat","sleep","repeat"] 
for ele in enumerate(l1): 
    print(ele )


print()
for ele in enumerate(l1,100): 
    print(ele )


print("\n\n\n\n\n\n")





#Any itratable object can be converted to list using list()
str="90"
print(list(str))
list1 = [1, 3, 4, 1]
print("maximum is",max(list1))
print("minimum is",min(list1))
print("sum is",sum(list1))
print("sorted list is ",sorted(list1))
#just returns the sorted list, doesn't modify the source.
print(list1)



print("\n\n\n\n\n\n")


list2=[1,2,3,4,5]
print(list2)
list2.clear()
print(list2)
print("\n\n\n\n\n\n")




