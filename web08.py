import requests
data = {
        'username' : 'admin',
        'password' : 'admin'
        }
url = 'http://web-08.challs.olicyber.it/login'
print(requests.post(url, data=data).text)
