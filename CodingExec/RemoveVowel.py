#Remove vowels from sepcified string

def remove_vowels(string):
    newString = string
    vowels = ('a','e','i','o','u')
    for c in string.lower():
        for c in vowels:
            newString = newString.replace(c, '')
    return newString

print('Enter x for exit')
string = input('Enter any string to remove all vowels from it')
if string == 'x':
    exit
else:
    print('The new string after removing  the vowels' + remove_vowels(string))
