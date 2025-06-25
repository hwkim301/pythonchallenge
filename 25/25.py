import requests
from PIL import Image
import wave

for i in range(1, 26):
    res = requests.get(
        f"http://www.pythonchallenge.com/pc/hex/lake{i}.wav", auth=("butter", "fly")
    )
    with open(f"lake{i}.wav", "wb") as f:
        f.write(res.content)


img = Image.new("RGB", (300, 300))

with wave.open("lake1.wav", "rb") as f:
    total_bytes = f.getnframes()

for i in range(1, 26):
    with wave.open(f"lake{i}.wav", "rb") as wf:
        data = wf.readframes(total_bytes)

        parts = Image.frombytes("RGB", (60, 60), data)

        idx = i - 1
        col = (idx % 5) * 60
        row = (idx // 5) * 60

        img.paste(parts, (col, row))

img.save("level25.png")
