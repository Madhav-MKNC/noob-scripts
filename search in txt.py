import os
import madhavmodule1 as mm

path = os.getcwd()
files = []
element = input("what do you wanna search: ")

for file in os.listdir(path):
    if file.endswith(".txt"):
        print("text files: ",file)
        if element in list(open(os.path.join(path,file),'r').readlines()):
            print(file)