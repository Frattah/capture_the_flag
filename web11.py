import requests
import json as j

url = 'http://web-11.challs.olicyber.it'
json = {
        'username' : 'admin',
        'password' : 'admin'
        }
flag = ""
for i in range (0,4):
        session = requests.Session()
        resp = session.post(url + '/login', json=json)
        r = session.get(url + '/flag_piece?index=' + str(i) + '&csrf=' + str(j.loads(resp.text)['csrf']))
        flag += j.loads(r.text)['flag_piece']
print(flag)
        