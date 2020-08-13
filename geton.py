import requests 
import argparse
from threading import Thread

print('\n')
print('YET ANOTHER DIRECTORY BRUTE FORCE')
print('\n')

parser = argparse.ArgumentParser(description='Yet another directory brute force')

parser.add_argument('-u', '--url',help="Url to brute force",required=True)
parser.add_argument('-w', '--word',help="Wordlist to use",required=True)
parser.add_argument('-t', '--threads',help="Number of threads to use",default=10)

arg = parser.parse_args()

import time

class scanThread (Thread):

	def __init__(self, url, words):
		Thread.__init__(self)
		self.url = url
		self.words = words

	def run(self):

		for i in range(0,len(self.words)):

			self.words[i] = self.words[i].strip('\n')
			self.words[i] = self.words[i].strip(',')

			URL = self.url + "/" + self.words[i] + "/"
			response = requests.get(url = URL) 

			percentage = int(i / len(self.words) * 100)
			print('\r' + str(percentage) + "%",flush = False,end = '')
			if response.status_code == 200 :
				print('\r' + str(response.status_code) + " | " + URL + " -> " + response.url)

def scan():
	try:
		file = open(arg.word, "r")
		contents = file.readlines()
	except:
		print('Error opening the wordlist file')
		return

	threadsNumber = int(arg.threads)
	fullLength = len(contents)
	halfLength = int(len(contents) / threadsNumber)
	rest = len(contents) % threadsNumber
	start = 0
	threads = []

	for i in range(0,threadsNumber):
		thread = scanThread(arg.url, contents[start:start+halfLength])
		threads.append(thread)
		start+=halfLength
		if i == threadsNumber - 2 : start+=rest
		thread.start()
	for i in range(0,len(threads)-1):
		threads[i].join()


if __name__ == '__main__':
	scan()
