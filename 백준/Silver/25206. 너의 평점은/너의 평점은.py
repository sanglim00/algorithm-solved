import sys

gpa_sum = 0
credit_sum = 0
for _ in range(20):
    classname, credit, gpa = sys.stdin.readline().split()
    credit = float(credit)
    num = 0
    if gpa == 'A+': num = 4.5
    elif gpa == 'A0': num = 4.0
    elif gpa == 'B+': num = 3.5
    elif gpa == 'B0': num = 3.0
    elif gpa == 'C+': num = 2.5
    elif gpa == 'C0': num = 2.0
    elif gpa == 'D+': num = 1.5
    elif gpa == 'D0': num = 1.0
    elif gpa == 'F': num = 0

    gpa_sum += credit * num 
    if gpa != 'P': credit_sum += credit 

print(format(gpa_sum/credit_sum, '.6f'))