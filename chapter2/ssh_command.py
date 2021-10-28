import pexpect
import time

PROMPT = ['#', '>>> ', '> ', '\$ ']

def send_command(child, cmd):
    child.expect(PROMPT)
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before.decode())

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    conn_str = f'ssh {user}@{host}'
    child = pexpect.spawn(conn_str)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    
    if ret == 0:
        print('[-] Error Connecting')
        return

    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
        if ret == 0:
            print('[-] Error Connecting')
            return
    
    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
    host = 'localhost'
    user = 'root'
    password = 'toor'

    conn = connect(user, host, password)
    send_command(conn, 'echo blabla')


if __name__ == "__main__":
    main()
