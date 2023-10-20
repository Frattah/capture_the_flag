import requests
url = 'http://web-02.challs.olicyber.it/server-records'
params = {'id':'flag'}
print(requests.get(url, params=params).text)

# We send a GET http request adding the id variable with 'flag' value.