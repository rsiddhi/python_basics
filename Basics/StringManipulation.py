print('Python String Manipulation')
print('--------------------------')

string1 = '\'I\'m good today\''
string2 = "\"I'm good today\""
print('string1= ' + string1)
print('string2= ' + string2)
print('string1 == string2: ' + str(string1 == string2))
print('\nprint(Today\\tis\\ta\\tgood\\tday)')
print('Today\tis\ta\tgood\tday')

print('for multiple line: print(\'\'\'...text goes here...\'\'\')')
msg = '''Hello
My name is Adam
I am 20 years old.
And I like to cooking.'''

print(msg)

print('\n')

string1 = "Python string manipulation"
print('string1= ' + string1)
print("'Python' in string1: " + str('Python' in string1))
print("'python' in string1: " + str('python' in string1))
print("'Java' not in string1: " + str('Java' not in string1))
print("string1.index('string'): " + str(string1.index('string')))

print('\n')

string2 = "Today is a nice day"
print("string2 = " + string2)
print("string2.lower(): " + string2.lower())
print("string2.upper(): " + string2.upper())
print("string2.title(): " + string2.title())

print('\n')

string3 = "have a nice day"
print("string3 = " + string3)
print("string3.islower(): " + str(string3.islower()))
print("string3.isupper(): " + str(string3.isupper()))
print("'123'.islower(): " + str('123'.islower()))
print("'123'.isupper(): " + str('123'.isupper()))

print('\n')

string4 = "My name is Jessica"
print("string4 = " + string4)
print("string4.startswith('My'): " + str(string4.startswith('My')))
print("string4.endswith('bye'): " + str(string4.startswith('bye')))

print('\n')

nameList = ['Harry', 'James', 'Cristina', 'Liam']
print("nameList = " + str(nameList))
print("''.join(nameList): " + str(''.join(nameList)))
print("','.join(nameList): " + str(','.join(nameList)))
print("'|'.join(nameList): " + str('|'.join(nameList)))

print('\n')
string5 = "My name is Peter"
print("string5 = " + string5)
print("string5.split(): " + str(string5.split()))

print('\n')
string6 = "My, name, is, Peter"
print("string6 = " + string6)
print("string6.split(','): " + str(string6.split(',')))

print('\n')
string7 = '''Hello
My name is Harry.
I am 25 years old'''
print('string7 = ' + string7)
print("string7.split('\Documents and Settings\n'): " + str(string7.split('\n')))

print('\n')
string8 = "    Kristina Dsuza   "
print("string8 = '" + string8 + "'")
print("string8.strip(): " + string8.strip())




