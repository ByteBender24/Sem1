


#maximum of a list
list=[12,11,31,41,22]
max=list[0]
for i in list:
  if i>max:
    max=i
print(max)


#sum of a list
list=[12,11,31,41,22]
sum=0
for i in list:
  sum=sum+i
print(sum)


#find index position
list=[12,11,31,41,22]
value=31
flag=0
for i in range(0,len(list)):
    if(list[i]==value): 
      print("index position",i)
      flag=1
      #break
if (flag==0):
    print("element not found")


#duplicate elimination
list=[12,11,31,41,11,31,22,12]
list1=[]
for i in list:
    if i not in list1:
        list1.append(i)
print(list1)


#even numbers within a limit
n=30
list1=[]
for i in range(1,n+1):
    if(i%2==0):
        list1.append(i)
print(list1)


#convert to upper
def upper_all(t):
    new_li=[]
    for i in t:
        new_li.append(i.upper())
    return new_li
s=['hello','world']
p=upper_all(s)
print(p)


#filter only upper cases
def only_upper(t):
    new_li=[]
    for i in t:
        if i.isupper():
            new_li.append(i)
    return new_li
print(only_upper(['a','b','C','D']))


#largest from inputs
li=[]
for i in range(5):
    num=int(input("Enter Number {}:".format(i+1)))
    li.append(num)


large=li[0]    
for j in range(1,len(li)):
    if large<li[j]:
        large=li[j]


print(large)



#search
def sequentialSearch(alist, key):
    for j in range(len(alist)):
            if alist[j] == key:
              return j
    return -1


n=int(input('Enter the total numbers'))
testlist = []
for i in range(n):
  num=int(input("Enter {}th value  ".format(i)))
  testlist.append(num ) 
item=int(input('Enter the item to be searched'))
val=sequentialSearch(testlist, item)
if val==-1:
    print('item not found')
else:
    print(item,' found in ',val,'th position')

