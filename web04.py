import requests
url = 'http://web-04.challs.olicyber.it/users'
headers = { 'Accept' : 'application/xml' }
page = requests.get(url, headers = headers).text
print(page[page.find('flag{') : page.find('}') + 1])
