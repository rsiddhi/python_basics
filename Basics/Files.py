print("Python file commands")
print('--------------------')

import os

print("os.getcwd() # return current directory path")
print("os.chdir() # changes to specified path")
print("os.makedirs() # makes new folder")
print("os.path.abspath('C:\\Users\\John\\Desktop\\PythonExecrise') # gives fullpath for the specified path/file/directory")
print("os.path.isabs() # checks specified path is an absolute path")
print("file = open('file.txt', 'r') # opens file for reading")
print("file.read() # returns text in the file")
print("file = open('file.txt', 'w' # open file for writing")
print("file.write('Hello, there')")
print("file.close() #closes the file")


os.chdir('D:\\tmp')
print(os.getcwd())

file = open('file.txt', 'a')
file.write("\nHave a nice day!!!")

file = open('file.txt', 'r')
for line in file.readlines():
    print(line)

file.close()
