import requests
from bs4 import BeautifulSoup

html_doc = requests.get('http://web-12.challs.olicyber.it/').text
soup = BeautifulSoup(html_doc, 'html.parser')
flag = soup.find_all('pre')[0].get_text()
print(flag[flag.find('flag{') : flag.find('}') + 1])