import requests 
import urllib 
import xmlrpc.client
import bz2

busynothing=12345
gathering=[]

while True:
    res=requests.get(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={busynothing}")
    busynothing=res.text.split(" ")[-1]
    cookies=res.cookies
    print(cookies)
    gathering.append(cookies.get('info'))
    if "busynothing is" not in res.text:
        break

print(gathering)
print("".join(gathering))


deflated=urllib.parse.unquote_to_bytes(b"BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0%20%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90")
print(deflated) # BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0%20%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90


print(bz2.decompress(deflated)) # b'is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.'


class MyTransport(xmlrpc.client.Transport):
    accept_gzip_encoding = False 

conn = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php", transport=MyTransport())

print(conn.system.listMethods()) # ['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities

print(conn.phone("Leopold")) # 555-VIOLIN

res=requests.get("http://www.pythonchallenge.com/pc/stuff/violin.php",cookies={"info":"the flowers are on their way"})
print(res.text)