import requests
from bs4 import BeautifulSoup

url = 'http://web-12.challs.olicyber.it/'
resp = requests.get(url).text
soup = BeautifulSoup(resp, 'html.parser')
flag = soup.find_all('pre')[0].get_text()
print(flag[flag.find('flag{') : flag.find('}') + 1])

# We do a simple GET request, then using the BeautifulSoup module we scan the resp
# to find the flag in the 'pre' tag.