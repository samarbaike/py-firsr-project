grade_A=0
grade_B=0
grade_C=0
grade_D=0
grade_F=0
n=int(input("Enter number of subjects: "))
for me in range(n):
    me=1
    points=int(input('Subject score in percentage: '))
    if 100>=points>=90:
        grade_A+=me
    elif 89>=points>=75:
        grade_B+=me
    elif 74>=points>=60:
        grade_C+=me
    elif 59>=points>=50:
        grade_D+=me
    elif 49>=points>=0:
        grade_F+=me
    else:
        print('Please enter a valid score!')
#Just some random function, don't mind it
def round10(x):
    rounding=round(x*100)/100
    return rounding


#PRINTING!!!
#A
if grade_A==0 or grade_A==1:
    print('A: ', grade_A, ' grade ', "(",round10(grade_A/n*100),"%",")", sep='')
else:
    print('A: ', grade_A, ' grades ', "(",round10(grade_A/n*100),"%",")", sep='')

#B
if grade_B==0 or grade_B==1:
    print('B: ', grade_B, ' grade ', "(",round10(grade_B/n*100),"%",")", sep='')
else:
    print('B: ', grade_B, ' grades ', "(",round10(grade_B/n*100),"%",")", sep='')

#C
if grade_C==0 or grade_C==1:
    print('C: ', grade_C, ' grade ', "(",round10(grade_C/n*100),"%",")", sep='')
else:
    print('C: ', grade_C, ' grades ', "(",round10(grade_C/n*100),"%",")", sep='')

#D
if grade_D==0 or grade_D==1:
    print('D: ', grade_D, ' grade ', "(",round10(grade_D/n*100),"%",")", sep='')
else:
    print('D: ', grade_D, ' grades ', "(",round10(grade_D/n*100),"%",")", sep='')

#F
if grade_F==0 or grade_F==1:
    print('F: ', grade_F, ' grade ', "(",round10(grade_F/n*100),"%",")", sep='')
else:
    print('F: ', grade_F, ' grades ', "(",round10(grade_F/n*100),"%",")", sep='')