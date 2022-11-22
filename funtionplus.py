


''''
def mnti(a,b):
    c=a-b
    return c
def kou(a,b):
    c=a*b
    return c
def han(a,b):
    c=a/b
    return c
def plus(a,b):
    c=a+b
    return c
n1=int(input('enter n1: '))
n2=int(input('enter n2: '))

k=input('enter = (-) (*) (/) (+) ')

if k=="-":
    print(f'{n1}-{n2}= {mnti(n1,n2)}')
elif k=="*":
      print(f'{n1}*{n2}= {kou(n1,n2)}')
elif k=="/":
      print(f'{n1}*{n2}= {han(n1,n2)}')
elif k=="+":
    print(f'{n1}+{n2}={plus(n1,n2)}')
else:
    print("Error plass enter + - * / ") '''



def mnti(a,b):
    c=a-b
    
    return c
def kou(a,b):
    c=a*b
    return c
def han(a,b):
    c=a/b
    return c
def plus(a,b):
    c=a+b
    return c
n1=int(input('enter n1: '))
n2=int(input('enter n2: '))

k=input('enter = (-) (*) (/) (+) ')
if k=='+' or k=='-' or k=='*' or k=='/':
    print(f'{n1}{k}{n2}=',end='')
    if k=='+':
        print(plus(n1,n2))
    elif k=='-':
        print(mnti(n1,n2))
    elif k=='*':
        print(kou(n1,n2))
    elif k=='/':
        print(han(n1,n2))
else:
    print('Error')

        
