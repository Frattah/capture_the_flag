import requests
url = 'http://web-10.challs.olicyber.it/'
# print(requests.options(url).headers)
print(requests.post(url).headers['X-Flag'])

# Using a OPTIONS request we find that we can use a POST method to get the
# value of 'X-flag' variable.