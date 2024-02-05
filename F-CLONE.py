import os, sys, platform,time
bit = platform.architecture()[0]
if bit == '64bit':
    import i
    os.system('clear')
    os.system('git pull')
   # os.system('python F-CLONE.so')
else:
    exit()
