import requests
cookies = {'password' : 'admin'}
url = 'http://web-06.challs.olicyber.it'
r1 = requests.get(url + '/token')
print(requests.get(url + '/flag', cookies = r1.cookies).text)

# We send a GET http request to the 'token' resource so we can obtain a session cookie,
# then we can send a second GET http request but on the 'flag' resource