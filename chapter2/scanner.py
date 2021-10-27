import argparse
import socket

def conn_scan(ip, port):
    try:
        conn_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_skt.connect((ip, port))
        conn_skt.send('Dataaaaa\r\n'.encode())
        results = conn_skt.recv(100)
        print(f'[+] {port}/tcp ouvert')
        print(f'[+] {results}')
        conn_skt.close()
    except Exception as e:
        print(f'[-] {port}/tcp ferme : {e}')




def port_scan(dest, port):
    try:
        ip = socket.gethostbyname(dest)
    except:
        print(f'[-] Ne peut pas resoudre {dest} : Unknown host')
        return
    try:
        dest_name = socket.gethostbyaddr(ip)
        print(f'[+] Resultat de scan pour : {dest_name[0]}')
    except:
        print(f'[+] Resutlat de scan pour : {ip}')
    socket.setdefaulttimeout(1)
    for ports in port:
        print(f' Scanning port {ports}')
        conn_scan(ip, int(ports))




def main():
    #Argparse
    parser = argparse.ArgumentParser(description='A port scanner',
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    usage = 'scanner.py -d <tgtHost> -p <tgtPort>')
    parser.add_argument('-d','--dest', help='Destination Hostname', required=True)
    parser.add_argument('-p','--port', help='Destination Port', required=True, nargs='+')
    args = parser.parse_args()
    port_scan(args.dest, args.port)

if __name__ == '__main__':
    main()
