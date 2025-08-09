"""
calculator.py

This is a simple python calculator that performs basic operations such as addition, subtraction, etc.
"""

CHECK='y'
while CHECK=='y' :
    a=int(input('Enter first number: '))
    op=input("Choose operation: + , - , * , / , %, ^ : ")
    b=int(input('Enter second number: '))

    if op=='+' :
        result=a+b
    elif op=='-' :
        result=a-b
    elif op=='*' :
        result=a*b
    elif op=='/':
        result=a/b
    elif op=='%' :
        result=a%b
    elif op=='^' :
        result=a**b
    else:
        print('Choose valid operator')
        continue
    print(a,op,b,'=',result)
    CHECK=input("Do you want to calculate again: y , n")
