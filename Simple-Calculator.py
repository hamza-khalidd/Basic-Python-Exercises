# Input 2 No.s
# Select Operation

num1 = int(input('Enter Num 01: '))
num2 = int(input('Enter Num 02: '))

print('Select Operator: \n + (For Addition) \n - (For Substraction) \n * (For Multiplication) \n / (For Division)')
op = input('Enter Operator: ')

if op == '+':
    print('Addition: ', num1+num2)
if op == '-':
    print('Substraction: ', num1-num2)
if op == '*':
    print('Multiplication: ', num1*num2)
if op == '/':
    print('Division: ', num1/num2)