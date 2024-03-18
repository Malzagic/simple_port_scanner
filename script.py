import socket
from termcolor import colored

def scan(target, ports):
  print("\n" + " Starting Scan For " + str(target))
  for port in range(1, ports):
    scan_port(target, port)

def scan_port(ipaddress, port):
  try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
    print("[+] Port opened " + str(port))
    sock.close()
  except:
    # print("[-] Port closed " + str(port))
    pass

targets = input("[*] Enter Targets to Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want to Scan: "))

if "," in targets:
  print(colored("[*] Scanning Multiple Targets", "green"))
  for ip_addr in targets.split(","):
    scan(ip_addr.strip(" "), ports)
else:
  scan(targets, ports)