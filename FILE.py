import os, sys, platform,time
bit = platform.architecture()[0]
if bit == '64bit':
    print('\n Your device is 64 bit')
    os.system('clear')
    os.system('git pull')
    import file_create
elif bit == '32bit':
    os.system('clear')
    os.system('git pull')
    os.system('python F.py')
    print(" Onky 64bit .. changing architecture...by importing F.py")
  #(" Sorry 364 Bit only \n Wait 
