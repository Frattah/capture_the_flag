import requests
cookies = {'password' : 'admin'}
url = 'http://web-06.challs.olicyber.it'
resp = requests.get(url + '/token')
print(requests.get(url + '/flag', cookies = resp.cookies).text)

# We send a GET http request to the 'token' resource so we can obtain a session cookie,
# then we can send a second GET http request but on the 'flag' resource