import requests 

res=requests.get("http://www.pythonchallenge.com/pc/return/evil2.gfx", auth=("huge", "file"))


print(len(res.content))

for i in range(5):
    with open(f"{i}.jpg", "wb") as f:
        f.write(res.content[i::5])