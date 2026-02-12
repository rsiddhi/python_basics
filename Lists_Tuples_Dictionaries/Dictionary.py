#Dictionaries - Values Items, Get

dictAge = {'Adam': 30, 'John': 20, 'Jessica': 25}
print('dictAge = ' + str(dictAge))
print('dictAge[\'Adam\']: ' + str(dictAge['Adam']))
print('len(dictAge): ' + str(len(dictAge)))
print('if \'Harry\' in dictAge:' + str('harry' in dictAge) + '# check if key exists')
print('for value in dictAge.values():')
for value in dictAge.values():
    print(value)
print('for key in dictAge.keys():')
for key in dictAge.keys():
    print(key)
print('get keys  with list:')
print('list(dictAge)' + str(list(dictAge)))
print('for item in dictAge.items():')
for item in dictAge.items():
    print(item)
print('for name, age in dictAge.items():')
for name, age in dictAge.items():
    print('The age of ' + name + ' is ' + str(age) + ' years')

personName = input('Enter a name:');
print('dictAge.get(\'' + personName + '\'): ' + str(dictAge.get(personName, 0)) + ' years')



