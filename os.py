import os
import re


print(os.getcwd())
print(os.listdir())
f1 = os.listdir()
print(f1.sort())
listtxt = open('./list.txt','a')
for file in f1:
    fileType = os.path.split(file)
    print(fileType)
    if fileType[1] == '.py':
        continue
    name = file + ' ' + str(int(1)) + '\n'
    listtxt.write(name)
listtxt.close()

print(os.path.join(os.getcwd(),'Other'))

s = ['Bunner.mp4','Other.mp4','Fitghting_12ed3.mp4']
s.sort()
print(s)
