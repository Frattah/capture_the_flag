import requests
from bs4 import BeautifulSoup

def find_list_resources (tag, attribute,soup):
   list = []
   for x in soup.findAll(tag):
       list.append(x[attribute])
   return(list)

url = 'http://web-15.challs.olicyber.it/'
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'html.parser')
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
external = [i for i in external if i != []]
html_doc = ''
for i in external:
    html_doc += requests.get(url + i[0]).text
print(html_doc[html_doc.find('flag{') : html_doc.find('}') + 1])