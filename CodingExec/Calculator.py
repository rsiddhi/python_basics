# Python Calculator

print('Enter a choice for a calculation or x to exit')

print('1, Addition')
print('2, Subtraction')
print('3, Multiplication')
print('4, Division')

while True:
    choice = input('Enter Choice:')

    exits = choice in '1234'
    if choice == 'x':
        break

    if exits:
        num1 = int(input('Enter first number:'))
        num2 = int(input('Enter second number:'))
    else:
        print('Enter a valid choice')
    match choice:
        case '1':
            print('add ' + str(num1+num2))
        case '2':
            print('sub' + str(num1-num2))
        case '3':
            print('mul'+ str(num1*num2))
        case '4':
            print('div '+str(num1/num2))

print('Closing the program')
        
