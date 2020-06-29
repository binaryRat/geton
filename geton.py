import requests 
import argparse

parser = argparse.ArgumentParser(description='Makes a GET request to a specified url and prints the response text.')

parser.add_argument('-u', '--url',help="Url to GET",required=True)
parser.add_argument('-w', '--word',help="Wordlist to use",required=True)

arg = parser.parse_args()

file = open(arg.word, "r")
contents = file.readlines()

for i in range(0,len(contents)):

	contents[i] = contents[i].strip('\n')
	contents[i] = contents[i].strip(',')

	PARAMS ={}

	URL = arg.url + "/" + contents[i] + "/"

	response = requests.get(url = URL, params = PARAMS) 
	#response = requests.post(url = arg.url, params = PARAMS) 
	print('\r' + str(i) + "/" + str(len(contents)),flush = False,end = '')
	if response.status_code == 200 :
		print('\r' + URL + " -> " + response.url + " | " + str(response.status_code) + " | " + str(response.elapsed))
		#print(r.text)


