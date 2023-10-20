import requests
url = 'http://web-07.challs.olicyber.it/'
resp = requests.head(url)
print(resp.headers['X-Flag'])

# We send a HEAD request to find the value of 'X-Flag' variable