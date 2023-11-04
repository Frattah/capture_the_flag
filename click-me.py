import requests

url = 'http://click-me.challs.olicyber.it/'
cookies= {
        'cookies' : '10000000'
    }
resp = requests.get(url, cookies=cookies)
print(resp.text[resp.text.find('flag{') : resp.text.find('}') + 1])