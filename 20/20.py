import requests
import zipfile 

nextval = 30203
res = requests.get(
    "http://www.pythonchallenge.com/pc/hex/unreal.jpg",
    auth=("butter", "fly"),
    headers={"Range": "bytes=30203-2123456789"},
)
print(res.text, len(res.text))

nextval = nextval + len(res.text)
res = requests.get(
    "http://www.pythonchallenge.com/pc/hex/unreal.jpg",
    auth=("butter", "fly"),
    headers={"Range": f"bytes={nextval}-2123456789"},
)
print(res.text, len(res.text))


while True:
    nextval = nextval + len(res.text)
    res = requests.get(
        "http://www.pythonchallenge.com/pc/hex/unreal.jpg",
        auth=("butter", "fly"),
        headers={"Range": f"bytes={nextval}-2123456789"},
    )
    print(res.text)
    if len(res.text) == 0:
        break

res = requests.get(
    "http://www.pythonchallenge.com/pc/hex/unreal.jpg",
    auth=("butter", "fly"),
    headers={"Range": "bytes=2123456744-"},
)
print(res.text, len(res.text))
print(res.headers)


res = requests.get(
    "http://www.pythonchallenge.com/pc/hex/unreal.jpg",
    auth=("butter", "fly"),
    headers={"Range": "bytes=2123456743-"},
)
print(res.text, len(res.text))
print(res.headers)

res = requests.get(
    "http://www.pythonchallenge.com/pc/hex/unreal.jpg",
    auth=("butter", "fly"),
    headers={"Range": "bytes=1152983631-"},
)
print(res.text, len(res.text))
print(res.headers)

with open("blob", "wb") as f:
    res = requests.get("http://www.pythonchallenge.com/pc/hex/unreal.jpg",auth=("butter", "fly"),headers={"Range": "bytes=1152983631-"})
    f.write(res.content)


with zipfile.ZipFile("blob.zip","r") as myzip:
    myzip.extractall(".",pwd=b"redavni")