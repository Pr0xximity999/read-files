import os
from time import sleep

path = os.getcwd()
readMe = open(path + '/read-files/README.md', 'r')
content = readMe.read()

for i in content.split('.'):
    print(i + '.') if i != content.split('.')[-1] else print(i)
    sleep(1)
