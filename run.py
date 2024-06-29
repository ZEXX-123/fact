#coding=utf-8
import os, sys, platform
os.system('rm -rf zexx')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf zexx')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('zexx'):
        os.system('curl -L https://github.com/ZEXX-123/fact/blob/main/zexx?raw=true -o zexx')
        os.system('chmod 777 zexx;./zexx')
    else:
        os.system('chmod 777 zexx;./zexx')
