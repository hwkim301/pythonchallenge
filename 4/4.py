import requests

nothing = 12345
while True:
    res = requests.get(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}")
    nothing = res.text.split(" ")[-1]
    print(res.text)

    if "Yes." in res.text:
        nothing = 16044 // 2
        continue

    elif "next nothing is" not in res.text:
        break
