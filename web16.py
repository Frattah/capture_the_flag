import requests
from bs4 import BeautifulSoup
import time

def find_list_resources (tag, attribute,soup):
   list = []
   for x in soup.findAll(tag):
       list.append(x[attribute])
   return(list)

def find_flag (link, seen): 

    # Find flag if it is here
    html_doc = requests.get(link).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    flag = soup.find_all('h1')[0].get_text()
    if flag.find('flag{') != -1:
        return flag[flag.find('flag{') : flag.find('}') + 1]
    else:
        # List all this page's link
        scan = find_list_resources("a","href",soup)
        # Append this url to 'seen' list
        parameter = '/' + link[len(link) - link[::-1].find('/'):]
        seen.append(parameter)
        # Eliminate parameter from url
        link = link[0 : len(link) - link[::-1].find('/') - 1]
        flag = ""
        for i in scan:
            if i not in seen:
                flag = find_flag(link + i, seen)
                if flag != "":
                    break
        return flag

url = 'http://web-16.challs.olicyber.it/page?p=1876933'
print(find_flag(url, []))
