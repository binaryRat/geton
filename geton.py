import requests 
import argparse

parser = argparse.ArgumentParser(description='Yet another directory brute force')

parser.add_argument('-u', '--url',help="Url to brute force",required=True)
parser.add_argument('-w', '--word',help="Wordlist to use",required=True)

arg = parser.parse_args()

def scan():
    try:
        file = open(arg.word, "r")
        contents = file.readlines()
    except:
        print('Error opening the wordlist file')
        return

    for i in range(0,len(contents)):

        contents[i] = contents[i].strip('\n')
        contents[i] = contents[i].strip(',')

        URL = arg.url + "/" + contents[i] + "/"

        response = requests.get(url = URL) 
             
        print('\r' + str(i) + "/" + str(len(contents)),flush = False,end = '')
        if response.status_code == 200 :
            print('\r' + URL + " -> " + response.url + " | " + str(response.status_code) + " | " + str(response.elapsed))
if __name__ == '__main__':
    scan()
