from concurrent.futures import thread
import random
import socket
from struct import pack
import threading
import os
os.system("cmd /c cls")
print("""
 ██▓███   ██▀███   ▒█████   ▄▄▄██▀ ▓█████  ▄████▄ ▄▄▄█████▓      ██████  ▄▄▄      ██▀███   ▀██ ▄█▀▓█████ ██▀███  
▓██░  ██ ▓██ ▒ ██▒▒██▒  ██▒   ▒██  ▓█   ▀ ▒██▀ ▀█ ▓  ██▒ ▓▒    ▒██    ▒ ▒████▄   ▓██ ▒ ██▒  ██▄█▒ ▓█   ▀▓██ ▒ ██▒
▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒   ░██  ▒███   ▒▓█    ▄▒ ▓██░ ▒░    ░ ▓██▄   ▒██  ▀█▄ ▓██ ░▄█ ▒ ▓███▄░ ▒███  ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░▓██▄██▓ ▒▓█  ▄▒▒▓▓▄ ▄██░ ▓██▓ ░       ▒   ██▒░██▄▄▄▄██▒██▀▀█▄   ▓██ █▄ ▒▓█  ▄▒██▀▀█▄  
▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░ ▓███▒ ▒░▒████░▒ ▓███▀   ▒██▒ ░     ▒██████▒▒ ▓█   ▓██░██▓ ▒██▒ ▒██▒ █▄░▒████░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░  ▒▓▒▒░ ░░░ ▒░ ░░ ░▒ ▒    ▒ ░░       ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ▒▓ ░▒▓░ ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▓ ░▒▓░
░▒ ░       ░▒ ░ ▒   ░ ▒ ▒░  ▒ ░▒░ ░ ░ ░     ░  ▒      ░        ░ ░▒  ░    ░   ▒▒   ░▒ ░ ▒░ ░ ░▒ ▒░ ░ ░    ░▒ ░ ▒░
░░         ░░   ░ ░ ░ ░ ▒   ░ ░ ░     ░   ░         ░          ░  ░  ░    ░   ▒     ░   ░  ░ ░░ ░    ░     ░   ░ 
            ░         ░ ░   ░   ░ ░   ░   ░ ░                        ░        ░     ░      ░  ░      ░     ░     
""")
print("made by Perchant76")
print("""
[1]-Port scanner
[2]-DDoSer
[3]-pinger
[4]-EXIT
""")

while 1<2:
	a1 = input(">")
	if a1 == "1":
		os.system("cmd /k portscanner.py")
	elif a1 == "2":
		os.system("cmd /k ddos.py")
	elif a1 == "4":
		#os.system("TASKKILL /F /IM cmd.exe")
		quit()
	elif a1 == "3":
		os.system("cmd /k pinger.py")
	else:
		print("unknown command :/")