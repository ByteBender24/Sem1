# 3. Consider the mark_list=[('Rams',120,55,45,65,45,32),
# ('Vel',121,94,86,78,67,90), ('Siri',122,73,98,90,87,89)]
# which contains the name, register number and marks of corresponding student
# as list of tuples. Create a new tuple that assigns a grade based on the following
# conditions:
# if Marks >=90 then grade A
# if Marks >=80 && <90 then grade B
# if Marks >65 && < 80 then grade C
# if Marks > =40 && <=65 then grade D
# Output:
# [('Rams',120,Grades),(.....)]

mark_list=[('Rams',120,55,45,65,45,32),('Vel',121,94,86,78,67,90), ('Siri',122,73,98,90,87,89)]
new_mark_list = []
for i in mark_list :
    new_mark = [i[0],i[1]]
    marks=0

    for j in range(2,len(i)):
        marks+=i[j]
    marks=marks/(len(i)-2)

    if marks >=90:
        new_mark.append("Grade A")
    elif 80<=marks<90:
        new_mark.append("Grade B")
    elif 65 < marks < 80:
        new_mark.append("Grade C")
    elif 40 <= marks <=65:
        new_mark.append("Grade D")
    elif marks<40:
        new_mark.append("Grade F")
    new_mark_list.append(tuple(new_mark))

print (new_mark_list)


