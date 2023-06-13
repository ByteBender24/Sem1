# Write a Python code to read the content of ‘ebook.txt’ and display the contents of the file
# onto the console. 


f1 = open('SSN exercises\Exercise 10\q1.txt','r')
for lines in f1.readlines():
    print (lines)

f1.close()


