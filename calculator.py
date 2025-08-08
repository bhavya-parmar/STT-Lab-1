c=0
ch='y'
while ch=='y' :
    a=int(input('Enter first number: '))
    b=int(input('Enter second number: '))
    op=input("Choose operation: + , - , * , / , %, ^ : ")
    c=0
    if op=='+' :
        c=a+b
    elif op=='-' :
        c=a-b
    elif op=='*' :
        c=a*b
    elif op=='/':
        c=a/b
    elif op=='%' :
        c=a%b
    elif op=='^' :
        c=a**b
    else:
        print('Choose valid operator')
    print(a,op,b,'=',c)
    ch=input("Do you want to calculate again: y , n")