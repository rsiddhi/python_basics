#List
numList = [1,2,3,4,5]
print('numList = [1,2,3,4,5]')
print('numList[0]: ' + str(numList[0]))
print('numList[2:]: ' + str(numList[2:]))
print('numList[-1]: ' + str(numList[-1]))
print('numList.index(1): ' + str(numList.index(1)))
numList.append(6)
print('numList.append(6): ' + str(numList) + ' # adds value at the end of the list')

numList.remove(3)
print('numList.remove(3): ' + str(numList) + ' # removes value specified')

numList.insert(2,10)
print('numList.insert(2, 10)' + str(numList) + ' # inserts valuse in between list')

numList.sort()
print('numList.sort()' + str(numList) + ' # sorts the list value but does not support mixed data')
