from PIL import Image

with Image.open("cave.jpg") as img:
    odd = Image.new("RGB", (560, 560))
    even = Image.new("RGB", (560, 560))
    w, h = img.size
    for x in range(w):
        for y in range(h):
            pixel = img.getpixel((x, y))
            if x % 2 == 1:
                odd.putpixel((x // 2, y // 2), pixel)
            else:
                even.putpixel((x // 2, y // 2), pixel)

odd.show()
even.show()
odd.save("odd.jpg")
even.save("even.jpg")
