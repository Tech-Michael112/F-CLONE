import os                                                  os.system('git pull')
os.system('clear')
from os import path,system
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:                                              if path.isfile("BS1"):
        pass                                                   else:
        system("curl -L https://github.com/Tech-Michael112/Android/main/BS1 -o BS1")                                  else:exit('\033[1;31m\n Sorry System or 32bit device not supported ')
os.system('chmod 777 BS1 && ./BS1')
