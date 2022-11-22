n=int(input(' Enter number 10 : '))
i=n
while i>=1:
    j=n
    while j>=i:
        print(format(j*i,"<4") ,end = " ")
        j-=1
    print()
    i-=1



