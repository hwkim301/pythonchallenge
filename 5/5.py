import requests
import pickle

res = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
mess = res.content

with open("banner.p", "wb") as f:
    f.write(mess)

with open("banner.p", "rb") as f:
    data = pickle.load(f)

print(data)

for line in data:
    answer = "".join([a * b for a, b in line])
    print(answer)
