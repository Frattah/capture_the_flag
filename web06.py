import requests
cookies = {'password' : 'admin'}
url = 'http://web-06.challs.olicyber.it'
r1 = requests.get(url + '/token')
print(requests.get(url + '/flag', cookies = r1.cookies).text)
