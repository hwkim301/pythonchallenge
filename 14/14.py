from PIL import Image


output_size = 100

with Image.open("wire.png") as im:
    out = Image.new("RGB", (output_size, output_size))

    x, y = -1, 0
    p = 0 

    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    d = 2 * output_size

    total_pixels = im.width * im.height

    while d // 2 > 0 and p < total_pixels:

        for dx, dy in dir:
            current_length = d // 2

            for _ in range(current_length):
                if p >= total_pixels:
                    break

                x += dx
                y += dy

                out.putpixel((x, y), im.getpixel((p, 0)))
                p += 1 

            if p >= total_pixels:
                break
            d -= 1

out.show()