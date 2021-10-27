import socket
import sys
import os

def retBanner(ip, port):
    print(f'[*] Connection a {ip}:{port}')
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        print(f'Erreur = {e}')
        return

def checkVulns(banner,filename):
    f = open(banner,mode='r')
    vuln = f.readlines()
    for lines in vuln:
        if lines.strip('\n') in banner:
            printf("[*] Serveur vulnerable : {banner}")


def main():
    if len(sys.argv)==2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print(f'[-] {filename} does not exist')
            exit(0)

        if not os.access(filename, os.R_OK):
            print(f'[-] {filename} access denied') 
            exit(0)

        for x in range(1,2):
            portList = [80]
            ip = "127.0.0." + str(x) 
            for port in portList:
                banner  = retBanner(ip,port)
                if banner:
                    print(f"[*] {ip}:{port} : {banner}")
                    checkVulns(banner,filename)

    else:
        print(f'[-] Usage : {str(sys.argv[0])} <vuln filename>')
        exit(0)

if __name__ == "__main__":
    main()
