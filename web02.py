import requests
url = 'http://web-02.challs.olicyber.it/server-records'
print(requests.get(url + '?id=flag').text)

# We send a GET http request adding the id variable with 'flag' value.