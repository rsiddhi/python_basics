dict1 = { 'a': 1, 'b': 2 , 'c': 6}
dict2 = { 'b': 3, 'c': 4 }
mergedDict = dict1 | dict2
print('dict1=' + str(dict1))
print('dict2=' + str(dict2))
print('dict1 | dict2:' + str(mergedDict) + " # merge two dictionaries")
dict1.pop('a')
print('dict1.pop(\'a\'):' + str(dict1) + '# returns and removes the element with specified key')
dict1.clear()
print('dict1.clear():' + str(dict1)+ '# remove all key/value pairs')
print('dict2.popitem():' +str(dict2.popitem()) + " # returns and removes the last inserted item') 

