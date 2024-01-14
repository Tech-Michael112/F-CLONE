import os, sys, platform,time
os.system('rm -rf new-user')
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    import BS1    
elif bit == '32bit':
    os.system('clear')
    os.system('git pull')
    import F
    os.system('python F.py')
  #(" Sorry 364 Bit only \n Wait for Mr==Michael To upload 32 Bit")
