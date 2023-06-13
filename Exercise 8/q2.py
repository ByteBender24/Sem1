# Consider a tuple as T = (1, 3, 2, 4, 6, 5). Write a program to store numbers
# present at odd index into a new tuple

T = (1,3,2,4,6,5)

odd_index = [T[x] for x in range(len(T)) if x%2!= 0]

print (tuple(odd_index))