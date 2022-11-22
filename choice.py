num1 = 7
num2 = 3
print(f'Value number1 = {num1} \nvalue number2 = {num2}')
print("PLEASE SELECT THIS:(  +  -  *  /  //  %  )")
chioce = str(input('ENTER THERE:'))

s1 = num1 + num2;
s2 = num1 - num2;
s3 = num1 * num2;
s4 = num1 / num2;
s5 = num1 // num2;
s6 = num1 % num2; 
if chioce =="+":
    print(f'{num1} + {num2} = {s1}');
elif chioce =="-":
    print(f'{num1} - {num2} = {s2}');
elif chioce =="*":
    print(f'{num1} * {num2} = {s3}');
elif chioce =="/":
    print(f'{num1} / {num2} = {s4}');
elif chioce =="//":
    print(f'{num1} // {num2} = {s5}');
elif chioce =="%":
    print(f'{num1} % {num2} = {s6}');
else:print("Eorr!");

