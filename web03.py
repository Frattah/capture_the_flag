import requests
url = 'http://web-03.challs.olicyber.it/flag'
headers = { 'X-Password' : 'admin' }
print(requests.get(url, headers=headers).text)

# We send a GET http request adding a X-Password variable with 'admin' as value
# to perform a primitive authentication procedure.