import requests
import bz2

res = requests.get("http://www.pythonchallenge.com/pc/ring/guido.html", auth=("repeat", "switch"))
hidden = res.text.splitlines()[12:]
data = [len(x) for x in hidden]
print(data)

print(bz2.decompress(bytes(data)))
