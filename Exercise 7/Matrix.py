# matrix formation
def get_matrix(r,c):
    mat=[]
    print("Enter matrix elements by row: ")
    for rows in range(r):
        temp=[]
        for cols in range(c):
            temp.append(int(input(f"[{rows}][{cols}]")))
        mat.append(temp)
    return mat

def disp_matrix(mat):
    r=len(mat)
    c=len(mat[0])
    for rows in range(r):
        for cols in range(c):
            print(mat[rows][cols],end=" ")
        print()


mat1=get_matrix(3,3)
print (mat1)
disp_matrix(mat1)

# #matrix addition
# def add_matrix(mat1,mat2):
#     add=[]
#     for rows in range(len(mat1)):
#         temp=[]
#         for cols in range(len((mat2)[0])):
#             temp.append(mat1[rows][cols]+mat2[rows][cols])
#             # print (temp)
#         add.append(temp)
#     return add


# mat1 =[[1,2],[0,0]]
# mat2 = [[4,4],[9,-1]]
# print(add_matrix(mat1,mat2))

#transpose of a matrix:
# def transpose_matrix(mat):
#     trans=[]
#     for r in range(len((mat)[0])):
#         temp=[]
#         for c in range(len(mat)):
#             temp.append(mat[c][r])
#         trans.append(temp)
#     print(trans)

# mat=[[1,2],[3,5],[9,0]]
# transpose_matrix(mat)

# x="global x"
# def outer():
#     x="outer x"
#     def inner():
#         nonlocal x
#         x="modified outer x"
#         print ("x from inner:",x)
#     inner()
#     print("X from outer:",x)
# outer()
# # print("X from main: ",x)

# X =[[12 , 7 ] , [ 4 , 5 ] , [ 3 , 8 ] ]
# # trans =[[X[ j ] [ i ] for j in range (len (X ) ) ]
# # for i in range (len (X[ 0 ] ) ) ]
# # print ( trans)


# for j in (len(X)):
#     for i in range(len(X[0])):
#         trans = X[j][i]
# print (trans)

# x=input("Enter word: ")
# y=[]
# a=0
# for i in x:
#     print(y)
#     if i in y:
#         a+=1
#         break
#     else:
#         pass  
#     y.append(i)
# if a==1:
#     print("Bad word")
# else:
#     print("Good word")