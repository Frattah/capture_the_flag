import requests
url = 'http://web-04.challs.olicyber.it/users'
headers = { 
        'Accept' : 'application/xml'    
        }
resp = requests.get(url, headers = headers).text
print(resp[resp.find('flag{') : resp.find('}') + 1])

# We send a GET http request adding the 'Accept' variable with 'application/xml' value