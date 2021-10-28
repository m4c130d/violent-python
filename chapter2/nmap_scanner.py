import nmap
import argparse

def nmap_scan(target_host, target_ports):
    nm_scan = nmap.PortScanner()
    for target_port in target_ports:
        nm_scan.scan(target_host, target_port)
        state = nm_scan[target_host]['tcp'][int(target_port)]['state']
        print(f'[*] {target_host} tcp/{target_port} {state}')

def main():
    parser = argparse.ArgumentParser(
            usage='nmap_scan.py TARGET_HOST -p TARGET_PORTS')
    parser.add_argument('host', type=str, metavar='TARGET_HOST',
                        help="specify target host's IP number")
    parser.add_argument('-p', type=str, metavar='TARGET_PORTS',
                        help='specify target port[s] seperated by comma '
                            '(no spaces)')
    args = parser.parse_args()

    args.ports = str(args.p).split(',')
    nmap_scan(args.host, args.ports)

if __name__ == "__main__":
    main()
