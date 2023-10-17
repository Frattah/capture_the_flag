import requests
from bs4 import BeautifulSoup

html_doc = requests.get('http://web-13.challs.olicyber.it/').text
soup = BeautifulSoup(html_doc, 'html.parser')
span = soup.find_all('span')
lett = []
for i in span:
    lett.append(i.get_text())
print('flag{' + ''.join(lett) + '}')

# We send a simple GET request and scanning the page we collect all highlithed letters
# Finally we join all letters to create the flag content