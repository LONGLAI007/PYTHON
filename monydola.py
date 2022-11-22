cash=int(input( "Enter you cash:"))
d100=cash//100
print(f'$100 : {d100}')
cash%=100
d50=cash//50
print(f'$50 :{d50} ')
cash%=50
d20=cash//20
print(f'$20 : {d20}')
cash%=10
d10=cash//10
print(f'$10 : {d10}')
cash%=5
d5=cash//5
print(f'$5 : {d5}')
cash%=2
d2=cash//2
print(f'$2 : {d2}')
print(f'$1 : {cash}')
total=d100+d50+d10+d5+d2+cash