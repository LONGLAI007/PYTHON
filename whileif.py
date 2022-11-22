n=int(input(' Enter number : '))
i=n
while i>=1:
    j=n
    while j>=i:
        print(format(j*i,"<3") ,end = " ")
        j-=1
    print()
    i-=1   