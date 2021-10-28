import argparse
import socket
import threading

screen_lock = threading.Semaphore(1)

def conn_scan(ip, port):
    try:
        conn_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_skt.connect((ip, port))
        conn_skt.send('Dataaaaa\r\n'.encode())
        results = conn_skt.recv(100)
        screen_lock.acquire()
        print(f'[+] {port}/tcp ouvert')
        print(f'[+] {results}')
    except Exception as e:
        screen_lock.acquire()
        print(f'[-] {port}/tcp ferme : {e}')
    finally:
        screen_lock.release()
        conn_skt.close()



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
        t = threading.Thread(target=conn_scan, args=(ip, int(ports)))
        t.start()



def main():
    #Argparse
    parser = argparse.ArgumentParser(description='A port scanner',
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    usage = 'scanner.py -d <tgtHost> -p <tgtPort>')
    parser.add_argument('-d','--dest', help='Destination Hostname', required=True)
    parser.add_argument('-p','--port', help='Destination Port', required=True, type=str)
    args = parser.parse_args()
    ports_parser = args.port.split(",")
    port_scan(args.dest, ports_parser)

if __name__ == '__main__':
    main()
