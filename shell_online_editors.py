from subprocess import getoutput as get 
import os 
import sys

while True:
    try:
        cwd = os.getcwd()
        command = input(f"{cwd}$ ")
        if not command: continue
        if command.lower() in ['exit','q']: sys.exit()
        if 'cd' == command.split()[0]:
            try:
                os.chdir(command.split()[1])
            except:
                print('No such directory found')
                print('='*50)
                continue
            output = f'changed directory to {os.getcwd()}'
        else: output = get(command)
        print('-'*50)
        print(output)
        print('='*50)
    except:
        print('!! error occured !!')
        print('=')*50
