import requests
url = 'http://web-01.challs.olicyber.it/'
print(requests.get(url).text)

# Using the requests module we do a GET http request and we can easily read the flag.