try:
    a = 3
    b = 9
    c = a/b
    print(str(a) + '/' + str(b) + ' = ' + str(c))
except ZeroDivisionError:
    print('Cant divide by zero')

try:
    fn = open('file.txt')
    fn.write('This is a text file')
except:
    print('Cant open the file')
else:
    print('Everithing is OK!!')


def convert(string):
    try:
        print(int(string))

    except ValueError as Arguement:
        print('cannot take integer value', Arguement)

a = 'www'
convert(a)
