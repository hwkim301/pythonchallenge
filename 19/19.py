import requests
import re
from base64 import b64decode
import soundfile

res = requests.get("http://www.pythonchallenge.com/pc/hex/bin.html", auth=("butter", "fly"))
boundary = re.escape(r"--===============1295515792==")
pattern = re.compile(f"{boundary}(.*?){boundary}", re.DOTALL)
match = pattern.search(res.text).group(1).strip("\n")
# print(match)

with open("blob","wb") as f:
    clean="".join(match.splitlines()[3:]).strip("\n").encode("utf-8")
    f.write(clean)

with open("india.wav","wb") as file:
    with open("blob","rb") as f:
        mess=f.read()
    file.write(b64decode(mess))

# data,samplerate=soundfile.read("india.wav")
# soundfile.write("new.wav",data,samplerate,endian="big")
