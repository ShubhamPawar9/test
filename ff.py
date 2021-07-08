import requests,random,string,time

def task():
	try:
		w = requests.post('https://qtalk.in/users/v1/verifyAnonymously',headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36'})
		toks = w.json()['accessToken']
	
	
		mhead = {
    "Host": "qtalk.in",
    "content-length": "132",
    "sec-ch-ua": "\"Google Chrome\";v\u003d\"89\", \"Chromium\";v\u003d\"89\", \";Not A Brand\";v\u003d\"99\"",
    "accept": "application/json, text/plain, */*",
    "x-auth-id-token-v2": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2MGU0YThkMzZmNDRhNzcyMjQ4NGI3NjMiLCJpYXQiOjE2MjU1OTgxNjMsImlzcyI6IlFUYWxrIiwicm9sZXMiOiJ1c2VyIiwibmJmIjoxNjI1NTk4MTYzLCJleHAiOjE2MjU1OTkwNjN9.3FcgiDRbTh3ACeEnLAL5275G-K27vGIJ6giEssS048A",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36",
    "x-web-client-version": "100000",
    "content-type": "application/json;charset\u003dUTF-8",
    "origin": "https://ssup.co",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://ssup.co/",
    "accept-language": "en-US,en;q\u003d0.9"
  }
		mhead['x-auth-id-token-v2'] = toks

		m = requests.post('https://qtalk.in/sessions/v1/open?shouldFetchOpenMetadata=true',headers=mhead,json={"collageId":"zFKI","webId":f"ec76d3097b7927eb62cc8e{''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))}","browserName":"Chrome","uuid":"ef79062b-6b97-460a-b833-75{''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))}"})
		print('Done')
	except:
		pass
	
while True:
	try:
		task()
		time.sleep(random.randint(0,7))
	except():
		print('error')
		pass
