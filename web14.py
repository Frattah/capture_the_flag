import requests
from bs4 import BeautifulSoup
from bs4 import Comment


resp = requests.get('http://web-14.challs.olicyber.it/')
soup = BeautifulSoup(resp.text, 'html.parser')
arr = soup.find_all(string=lambda text: isinstance(text, Comment))
for i in arr:
    flag = i[i.find('flag{') : i.find('}') + 1]
    if flag != '':
        break
print(flag)

# We send a GET http request and we scan to search the flag into comments
# This time we are using a special filtering and the Comment module