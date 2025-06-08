import zipfile

number = 90052
comments = []
while True:
    with open(f"{number}.txt", "r") as f:
        content = f.read()
    print(content)
    number = content.split()[-1]
    print(number)
    if number == "comments.":
        break
    with zipfile.ZipFile("channel.zip", "r") as myzip:
        print(myzip.getinfo(f"{number}.txt").comment.decode('utf-8'))
        comments.append(myzip.getinfo(f"{number}.txt").comment.decode('utf-8'))
print(comments)
print(*comments)