import re


txt = "This is my home."
x = re.findall('home', txt)
if x:
    print('found the string')
    print(x)
else:
    print('no match')

phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
string = "My Phone number is 111-444-7777 and Rita's phone number is 222-444-2222"
match = phoneNumber.findall(string)
if match:
    print('Search results: ' , match)
    for a in match:
        print(a)
else:
    print('no results')
