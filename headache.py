import requests
print(requests.head('http://headache.challs.olicyber.it/').headers['Flag'])