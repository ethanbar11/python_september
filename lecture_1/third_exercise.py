num1_as_text = input('Enter first number:')
num2_as_text = input('Enter first number:')
num1 = int(num1_as_text)
num2 = int(num2_as_text)
s = num1 + num2
if s > 0:
    print('The sum is positive!')
elif s == 0:
    print('The sum is zero!')
else:
    print('The sum is negative!')
