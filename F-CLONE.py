import os, sys, platform,time
bit = platform.architecture()[0]
if bit == '64bit':
    #mport i
    os.system('clear')
    os.system('git pull')
    os.system('python is_enc.py')
else:
    exit()
