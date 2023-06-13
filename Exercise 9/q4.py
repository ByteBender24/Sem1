'''
The names of students and a list of GPA's of two semesters of each student are in the dictionary data structure.
1. Write a function 'CGPA_stud' to calculate the CGPA of each student and return the computed information as a new dictionary.
2. Write a function 'display_names' that stores the details based on the ascending order of the student names
3. Write a function 'display_grade' that stores the details of the student based on the descending order of the CGPA.
4. Display the first three toppers
'''

#1

CGPA_studdict = {}
def CGPA_stud():
    global CGPA_studdict
    stud = input("Enter student name: ")
    num_sub = int(input("Enter number of subjects: "))
    marks = []
    for i in range(num_sub):
        marks.append(int(input()))
    j=0
    for i in marks:
        j = i + j
    CGPA = (j/num_sub) / 9.5
    CGPA_studdict[stud] = CGPA
    return CGPA_studdict

#2

def display_names():
    global CGPA_studdict
    for i in CGPA_studdict.keys():
        sorted_names = {i : CGPA_studdict[i] for i in list(sorted(CGPA_studdict.keys()))}
    return sorted_names

#3
sorted_marks = {}
def display_grade():
    global CGPA_studdict
    global sorted_marks
    # for i in CGPA_studdict.keys():
    for i in list(sorted(CGPA_studdict.values(),reverse = True)):       #cannot use .sort() as it returns None 
        for j in list(CGPA_studdict.keys()):
            if CGPA_studdict[j] == i:
                sorted_marks[j] = i
    return sorted_marks
                      
#4
def toppers():
    n=0
    for i in sorted_marks.keys():
        n=n+1
        print (i)
        if n==4:
            break


CGPA_stud()
display_names()
display_grade()
toppers()       

# #sorting with use of      
# from operator import itemgetter

# fruit_inventory = [("banana", 5), ("orange", 15), ("apple", 3), ("kiwi", 0)]

# fruits = dict(fruit_inventory)

# # Sort by key
# sorted(fruit_inventory, key=itemgetter(0))


# # Sort by value
# sorted(fruit_inventory, key=itemgetter(1))


# # sorted(fruit_inventory, key=itemgetter(2))

# print (fruits)
# print (str(fruits))
# # print (list(fruits))
# print (list(zip(fruits)))

    
    
    
