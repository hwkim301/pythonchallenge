import requests
import re

res = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
boundary = r"<!--(.*?)-->"

mess = "".join(re.findall(boundary, res.text, re.DOTALL))
answer = "".join(re.findall(r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", mess))
print(answer)  # linkedlist
