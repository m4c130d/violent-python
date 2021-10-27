import zipfile
import threading
import argparse

def extract_file(zFile, password):
    try :
        zFile.extractall(pwd=password.encode('utf-8'))
        print(f'[+] Found password = {password}')
        search = True
    except Exception as e:
        pass

def main():
    # Argparse
    parser = argparse.ArgumentParser(description='Un Cracker de fichier Zip',
                                    formatter_class=argparse.RawDescriptionHelpFormatter, 
                                    usage = ''' python3 zipcracker.py -f <file.zip> -w <wordlist>''')
    parser.add_argument("-w","--wordlist", help=argparse.SUPPRESS, required=True)
    parser.add_argument("-f","--file", help=argparse.SUPPRESS, required=True)
    args = parser.parse_args()

    zFile = zipfile.ZipFile(args.file)
    dictionary = open(args.wordlist)
    for line in dictionary.readlines():
        password = line.strip('\n')
        t = threading.Thread(target=extract_file, args=(zFile, password))
        t.start()

if __name__ == "__main__":
    main()
