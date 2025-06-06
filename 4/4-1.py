import requests

nothing = 0
while True:
    res = requests.get(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}")
    nothing = res.text.split(" ")[-1]
    print(res.text)
    if "next nothing is" not in res.text:
        break
