"""
installer/converter for Grabbit
REED 7/28/2019
"""

import subprocess
import sys
import time
import os
import threading
import shutil

dirpath = os.getcwd()

startupinfo = None
if os.name == 'nt':
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    
print("Attempting to install Pyinstaller, please wait...")
time.sleep(2)

subprocess.call([sys.executable, "-m", "pip", "install", "pyinstaller"])

print("Building Grabbit!.exe, please wait...")
time.sleep(2)

Gcommands = ["pyinstaller","--onefile" ,"--noconsole","--icon=grabbitbunny.ico", "Grabbit!.pyw"]
with subprocess.Popen( Gcommands, startupinfo=startupinfo,bufsize=0,stdout=subprocess.PIPE) as process:
    for line in iter(process.stdout.readline,b''):
        print(line)
            
print("Grabbit.exe has been built!\nBuilding updater.exe, please wait...")
time.sleep(2)

os.remove("Grabbit!.spec")
shutil.rmtree("__pycache__")
shutil.rmtree("build")
shutil.move(dirpath+"/dist/Grabbit!.exe", dirpath+"/Grabbit!.exe")
shutil.rmtree("dist")
time.sleep(2)

Ucommands = ["pyinstaller","--onefile" ,"--noconsole","updater.py"]
with subprocess.Popen(Ucommands, startupinfo=startupinfo,bufsize=0,stdout=subprocess.PIPE) as process:    
    for line in iter(process.stdout.readline,b''):
        print(line)

os.remove("updater.spec")
shutil.rmtree("__pycache__")
shutil.rmtree("build")
shutil.move(dirpath+"/dist/updater.exe", dirpath+"/updater.exe")
shutil.rmtree("dist")

print("updater.exe has been built! Thank you for using",end='\r')
time.sleep(.8)
sys.stdout.flush()
print("updater.exe has been built! Thank you for using.",end='\r')
time.sleep(.8)
sys.stdout.flush()
print("updater.exe has been built! Thank you for using..",end='\r')
time.sleep(.8)
sys.stdout.flush()
print("updater.exe has been built! Thank you for using...\n",end='\r')
time.sleep(.8)
sys.stdout.flush()
print(""" _____              _      _      _  _    _
|  __ \            | |    | |    (_)| |  | |
| |  \/ _ __  __ _ | |__  | |__   _ | |_ | |   //
| | __ | '__|/ _` || '_ \ | '_ \ | || __|| |  ('>
| |_\ \| |  | (_| || |_) || |_) || || |_ |_|  /rr
 \____/|_|   \__,_||_.__/ |_.__/ |_| \__|(_) *\))_
""")
time.sleep(1)
print("Downloading made easy!")
time.sleep(2.5)
