import os


n1=int(input("Enter your first number: "))
n2=int(input("Enter your second number: "))
print("1- Multiplication")
print("2- Division")
print("3- Subtraction")
print("4- Addition")
ch=int(input("Select operation: "))

def multiplication(x, y):
    product = x*y
    return product
m=multiplication(n1, n2)

def division(x, y):
    quotient = x/y
    return quotient
d=division(n1, n2)

def subtraction(x, y):
    difference = x-y
    return difference
s=subtraction(n1, n2)

def addition(x, y):
    sum = x+y
    return sum
a=addition(n1, n2)

os.system('cls' if os.name == 'nt' else 'clear')    

if ch==1:
    print(n1, '*', n2, '=', m)

elif ch==2:
    print(n1, '/', n2, '=', d)


elif ch==3:
    print(n1, '-', n2, '=', s)

elif ch==4:
    print(n1, '+', n2, '=', a)

else:
    print("Please, choose ONLY numbers from 1 to 4 for operation!!!")


