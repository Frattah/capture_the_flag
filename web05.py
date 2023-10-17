import requests
cookies = {'password' : 'admin'}
print(requests.get('http://web-05.challs.olicyber.it/flag', cookies=cookies).text)

# We send a GET http request adding a cookie variable 'password' with 'admin' as value
# to perform an authentication process.