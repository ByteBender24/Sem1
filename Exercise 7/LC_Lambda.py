# #lamda, map, filter


# def sqr(a):
#   return a**2


# result=sqr(5)
# print(result)


# print("---lamda---")
# result=lambda a:a**2
# print(result(5))


# #lambda function can take more than one arguments
# result2=lambda a,b:a*b
# print(result2(5,6))


# #map
# print("------map-----")
# list1=[1,2,3,4,5]
# y=list(map(sqr,list1))
# print(y)


# #map also takes lambda functions
# list1=[1,2,3,4,5,6]
# y=list(map(lambda a:a**2,list1))
# print(y)


# #filter
# print("-----filter---")
# def even(a):
#   return a%2==0


# list1=[1,2,3,4,5,6]
# y=list(filter(even,list1))
# print(y)


# y=list(filter(lambda a:a%2==0,list1))
# print(y)


# a=[1,2,3,4]
# b=[3,4,5,6]
# intersection=list(filter(lambda x:x in a , b))
# print(intersection)






# #reduce
# import functools
# list1=[1,2,3,4,5]
# a=functools.reduce(lambda b,c:b+c, list1)
# print(a)





# #list comprehension
# s=[x**2 for x in range(10)]
# print(s)


# V=[2**i for i in range(1,12)]
# print(V)


# list1=[1,2,3,4,5,6,7,8]
# M = [x for x in list1 if x%2==0]
# print(M)


# for i in range(1,101 ) : #the iterator
#   if int(i**0.5)== i**0.5: #conditional filtering 
#     print(i)


# perfsqre=[x for x in range(1,101) if int(x**0.5)== x**0.5]
# print(perfsqre)


#transpose
X = [[12,7],[4,5],[3,8]]
for i in range(len(X[0])):
  for j in range (len(X)):
    print(X[j][i],end=" ")
  print("")




#transpose of a matrix using list comprehension
X = [[12,7],[4,5],[3,8]]
trans =[[X[j][i] for j in range (len(X))] for i in range(len(X[0]))]
print(trans)
