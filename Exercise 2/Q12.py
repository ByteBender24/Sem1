BP=int(input("Enter the Basic Pay of the employee: "))
DA=0.88*BP
HRA=0.08*BP
CCA=1000
Insurance=2000
PF=0.1*BP

Gross_Pay=BP+DA+HRA+CCA
Deductions=Insurance+PF

Net_Salary=Gross_Pay-Deductions
print("\nThe net salary of the employee is:",Net_Salary)