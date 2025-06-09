import requests
import re

res = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")
boundary = r"<!--(.*?)-->"
mess = re.findall(boundary, res.text,re.DOTALL)[-1]
print(mess)
answer = "".join(re.findall(r"[a-zA-Z]", mess))
print(answer)
