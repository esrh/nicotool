import requests as r
from netrc import netrc
import keyring
import re

userid = netrc().authenticators("nicovideo")[0]
passwd = keyring.get_password('nicovideo', userid)
if passwd is None:
    keyring.set_password('nicovideo', userid, input("pass > "))
    
url = "https://secure.nicovideo.jp/secure/login?site=niconico"
data = {"mail":userid, "password":passwd}
data = r.post(url, data).text
nicoid = data[data.find('data-nico-userId="') + 18:].split('"', 1)[0]
print(nicoid)

url = "http://api.search.nicovideo.jp/api/v2/mylist_video/contents/search" 
data = r.get(url).text
print(data)

'''
x = re.match(r'data\-nico\-userId\="(.*)"', data)
if x:
    print(x.group()[0])
'''
