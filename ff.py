import requests,json
from bs4 import BeautifulSoup

sitemap = open(r'C:\Users\Shubham\Documents\sitemap925.txt', 'r')

for io in sitemap.readlines():
	reqs = requests.get(io)
	soup = BeautifulSoup(reqs.text, 'html.parser')
	print(soup)

	for link in soup.find_all('a'):
		ok = link.get('href')
		if '9to5mac.com' not in ok:
			if 'facebook.com' not in ok and 'youtube.com' not in ok and 'twitter.com' not in ok and 'instagram.com' not in ok and 'flipboard.com' not in ok:
				domain = (f'{ok}'.replace('https://','').replace('http://','').replace('https://www.','').replace('http://www.','').replace('www.','').split('/')[0])
				w = requests.get(f'https://panel.dreamhost.com/marketing/ajax.cgi?cmd=domreg-availability&domain={domain}')
				y = json.loads(w.text)
			
				if 'premium_price' in y:
					value = y['available']
					print(f'{domain}: {value}')
				else:
					pass
#	if '9to5mac.com' not in  link:
#		print(link.get('href'))