import requests
url = 'http://web-10.challs.olicyber.it/'
# print(requests.options(url).headers)
print(requests.post(url).headers['X-Flag'])
