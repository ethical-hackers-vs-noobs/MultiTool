import threading
import requests

websites = 	["http://www.google.com",
		"http://11non-existent-domain.net"]

def status_code(site):
	try:
		result = requests.get(site)
		print "[*] " + site + " " + str(result.status_code)
	except requests.exceptions.ConnectionError as e: 
		print "[*] " + site + " " + str(e[0][0])
	
for site in websites:
	t = threading.Thread(target=status_code, args=(site,))
	t.start()
