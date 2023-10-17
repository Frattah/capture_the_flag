import requests
json = {
        'username' : 'admin',
        'password' : 'admin'
        }
url = 'http://web-09.challs.olicyber.it/login'
resp = requests.post(url, json=json).text
print(resp[resp.find("flag{") : resp.find("}") + 1])
