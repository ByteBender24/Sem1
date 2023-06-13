'''
Create a dictionary for 6 employee details with empno as key, name, dob and net-pay as
list of values use appropriate dictionary methods:
a. Create a dictionary with the above information.
b. Insert a new employee details as the second employee
c. Delete the employee at the 4th position
d. Delete the last employee
e. Increment the salary of all employees by 5%
'''

emplo_det = {1: ['h', 'r', 10], 2: ['j', 's', 20], 3: ['k', 'o', 30]}

def employee_details():
    global emplo_det
    num_emp = int(input("Enter the number of employees: "))
    for i in range(num_emp):
        empno = int(input("Employee number: "))
        name = input("Name: ")
        dob = input("DOB as DD/MM/YY")
        net_pay = int(input("Enter netpay"))
        details = [name, dob, net_pay]
        emplo_det[empno] = details
    return emplo_det

# print (employee_details())

#2:

list_keys = list(emplo_det.keys())
n=0
for i in emplo_det.keys():
    n=n+1
    if n==2:
        employee_details()

# create the dictionary
employee_dict = {
    101: ['John', '01-02-1985', 50000],
    102: ['Mary', '15-05-1990', 60000],
    103: ['David', '28-09-1988', 55000],
    104: ['Linda', '11-12-1992', 65000],
    105: ['Peter', '02-03-1987', 70000],
    106: ['Sarah', '20-08-1995', 45000]
}

# print the initial dictionary
print("Initial Dictionary:\n", employee_dict)

# insert a new employee as the second employee
employee_dict[102] = ['Adam', '06-07-1993', 55000]

# delete the employee at the 4th position
del employee_dict[104]

# delete the last employee
employee_dict.popitem()

# increment the salary of all employees by 5%
for empno in employee_dict:
    employee_dict[empno][2] *= 1.05

# print the modified dictionary
print("\nModified Dictionary:\n", employee_dict)


