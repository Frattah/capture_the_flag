import requests
url = 'http://web-07.challs.olicyber.it/'
response = requests.head(url)
print(response.headers['X-Flag'])

# We send a HEAD request to find the value of 'X-Flag' variable