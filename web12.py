import requests
from bs4 import BeautifulSoup

html_doc = requests.get('http://web-12.challs.olicyber.it/').text
soup = BeautifulSoup(html_doc, 'html.parser')
flag = soup.find_all('pre')[0].get_text()
print(flag[flag.find('flag{') : flag.find('}') + 1])

# We do a simple GET request, then using the BeautifulSoup module we scan the html_doc
# to find the flag in the 'pre' tag.