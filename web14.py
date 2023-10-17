import requests
from bs4 import BeautifulSoup
from bs4 import Comment


html_doc = requests.get('http://web-14.challs.olicyber.it/').text
soup = BeautifulSoup(html_doc, 'html.parser')
arr = soup.find_all(string=lambda text: isinstance(text, Comment))
for i in arr:
    flag = i[i.find('flag{') : i.find('}') + 1]
    if flag != '':
        break
print(flag)