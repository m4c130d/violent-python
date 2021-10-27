import crypt
import sys

def test_pass(crypt_pass):
    salt = crypt_pass[:2]
    dict_file = open("dictionary.txt", 'r')

    for word in dict_file.readlines():
        word = word.strip('\n')
        crypt_word = crypt.crypt(word, salt)
        if crypt_pass == crypt_word:
            print(f'[+] Found password: {word}')
            return

    print('[-] Password not found')

def test_pass_sha512(crypt_pass):
    salt = crypt_pass[0:11]
    dict_file = open("dictionary.txt", 'r')

    for word in dict_file.readlines():
        word = word.strip('\n')
        crypt_word = crypt.crypt(word, salt)
        if crypt_word == crypt_pass:
            print(f'[+] Found password: {word}')
            return


if __name__ == '__main__':
    pass_file = open('shadow.txt')
    for line in pass_file:
        if ':' in line:
            user = line.split(":")[0]
            crypt_pass = line.split(":")[1].strip(' ')
            print(f'[*] Cracking password For: {user}')
            if "$6$" in crypt_pass:
                test_pass_sha512(crypt_pass)
            else:
                test_pass(crypt_pass)

