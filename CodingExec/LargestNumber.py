#Largest Number out of three

print('Find largest number out of three')
print('Enter x to exit')

while True:
    num1 = input('Enter frist number')
    if num1 == 'x':
        break
    else:
        num1 = int(num1)
        num2 = int(input('Enter second number'))
        num3 = int(input('Enter thrid number'))
        largest = num1;

        if largest < num2:
            if num2 > num3:
                largest = num2
            else:
                largest = num3
        elif largest < num3:
            if num3 < num2:
                largest = numb3
            else:
                largest = num2
        else:
            largest = num1
    if (num1 == num2 and num2 == num3):
        print('All three numbers are equal')
    else:
        print('Largest number is ' + str(largest))
            
            
