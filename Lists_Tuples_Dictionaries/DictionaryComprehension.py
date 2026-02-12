#Dictionaries Comprehension

dict1 = {'a':1, 'b': 2, 'c': 3}
dict2 = {k:v*2 for (k,v) in dict1.items()}
print(dict2)

newDict1={}
for n in range(10):
    if n%2 == 0:
        newDict1[n] = n**2

print(newDict1)

newDict2 = {}
newDict2 = {n:n**2 for n in range(10) if n%2 == 0}
print(newDict2)

if newDict1 == newDict2:
    print('True')
