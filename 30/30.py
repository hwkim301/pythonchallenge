from PIL import Image

with open("yankeedoodle.csv", "r") as f:

    data = [x.strip() for x in f.read().split(",")]
    print(data, len(data))

    img = Image.new("F", (53, 139))
    img.putdata([float(x) for x in data], 256)
    # img.show()
    img2 = img.transpose(Image.ROTATE_270)
    # img2.show()
    img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
    # img2.show()

    n = str(data[0])[5] + str(data[1])[5] + str(data[2])[6]
    print(n, bytes([int(n)]))

    answer = bytes(
        [
            (int(data[i][5] + data[i + 1][5] + data[i + 2][6]))
            for i in range(0, len(data) - 2, 3)
        ]
    )
    print(answer)

    a = data[0::3]
    b = data[1::3]
    c = data[2::3]

    answer2 = bytes(int(x[0][5] + x[1][5] + x[2][6]) for x in zip(a, b, c))
    print(answer2)

# b'So, you found the hidden message.\nThere is lots of room here for a long message, but we only need very little space to say "look at grandpa", so the rest is just garbage
