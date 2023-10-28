import requests
from bs4 import BeautifulSoup

def find_list_resources (tag, attribute,soup):
   list = []
   for x in soup.findAll(tag):
       list.append(x[attribute])
   return(list)

url = 'http://web-15.challs.olicyber.it/'
resp = requests.get(url).text
soup = BeautifulSoup(resp, 'html.parser')

# Find all external resources
external = []
external.append(find_list_resources("img","src",soup))   
external.append(find_list_resources("script","src",soup))
external.append(find_list_resources("link","href",soup))
external.append(find_list_resources("video","src",soup)) 
external.append(find_list_resources("audio","src",soup)) 
external.append(find_list_resources("iframe","src",soup))
external.append(find_list_resources("embed","src",soup))
external.append(find_list_resources("object","data",soup))         
external.append(find_list_resources("source","src",soup))

# Delete void entries
external = [i for i in external if i != []]
resp = ''
for i in external:
    resp += requests.get(url + i[0]).text
print(resp[resp.find('flag{') : resp.find('}') + 1])