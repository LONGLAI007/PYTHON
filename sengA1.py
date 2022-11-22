'''n=int(input(' Enter number : '))
i=n
while i>=1:
    j=n
    while j>=i:
        print(format(j*i,"<3") ,end = " ")
        j-=1
    print()
    i-=1    100-1'''


'''n=int(input("Enter number "))
i=n
while i >= 1 :
    j=1
    while j >= 1 :
        d = i*j
        while d >= 1:
            print(i*d, end=" ")
            d -= 1
        j -=1
    print()
    i -=1  '''
'''print("This is progame IQ cala")
num=int(input("enter number(>0):5"))
j=2
sum=0
for i in range(1,(num +1 )):
     sum=i*i*j
     print(f'{i}= {sum}')'''


print('This is Program IQ Calculate number.')
num1=int(input('Please enter number1 (>0): '))
num2=int(input('Please enter number1 (>0): '))
num3=num1*num2
rev = 0
while num3 != 0:
    b = num3 % 10
    rev = rev * 10 + b
    num3 //= 10
print(f'{num1} + {num2} = ', end="")
print(rev, end=" ")
print(b)


    