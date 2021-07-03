import requests,json
from bs4 import BeautifulSoup


okl = []
sitemap = open(r'sitemap925.txt', 'r')

for io in sitemap.readlines():
	reqs = requests.get((io).replace('\n',''))

	soup = BeautifulSoup(reqs.text, 'html.parser')

	for link in soup.find_all('a'):
		ok = link.get('href')
		if '9to5mac.com' not in ok:
			if 'facebook.com' not in ok and 'youtube.com' not in ok and 'twitter.com' not in ok and 'instagram.com' not in ok and 'flipboard.com' not in ok and '9to5' not in ok:
				domain = (f'{ok}'.replace('https://','').replace('http://','').replace('https://www.','').replace('http://www.','').replace('www.','').split('/')[0])
				w = requests.get(f'https://panel.dreamhost.com/marketing/ajax.cgi?cmd=domreg-availability&domain={domain}')
				y = json.loads(w.text)
			
				if 'premium_price' in y:
					value = y['available']
					if value == 'true':
						print(f'{domain}: {value}')
						okl.append(f'{domain}: {value}')
				else:
					pass
	print('Available ones:')
	print(okl)
#	if '9to5mac.com' not in  link:
#		print(link.get('href'))
