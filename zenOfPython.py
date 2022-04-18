import os
from time import sleep

path = os.getcwd()
content = open(path + '/read-files/README.md', 'r').readlines()

for i in content[1 : -1]:
    print(i)
    sleep(1)
