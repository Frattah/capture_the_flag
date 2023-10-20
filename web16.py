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
    resp = requests.get(link).text
    soup = BeautifulSoup(resp, 'html.parser')
    flag = soup.find_all('h1')[0].get_text()
    if flag.find('flag{') != -1:
        return flag[flag.find('flag{') : flag.find('}') + 1]
    else:

        # List all link of this page
        scan = find_list_resources("a","href",soup)

        # Append this resource to 'seen' list
        parameter = '/' + link[len(link) - link[::-1].find('/'):]
        seen.append(parameter)

        # Eliminate resource's reference from url
        link = link[0 : len(link) - link[::-1].find('/') - 1]
        flag = ""

        # Iterate on all scanned resource
        for i in scan:

            # But recurr only on 'not seen'
            if i not in seen:

                # Recurr on this resource
                flag = find_flag(link + i, seen)

                # You have find the flag, hence stop the iteration
                if flag != "":
                    break
        return flag

url = 'http://web-16.challs.olicyber.it/page?p=1876933'
print(find_flag(url, []))
