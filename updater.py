import os
os.system('taskkill /f /im Grabbit!.exe')
os.remove("Grabbit!.exe")
os.rename("Grabbit-UPDATE.exe","Grabbit!.exe")
os.startfile('Grabbit!.exe')
