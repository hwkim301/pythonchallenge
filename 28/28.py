from PIL import Image

with Image.open("bell.png") as img:
    r, g, b = img.split()
    greens = list(g.getdata())

pairs=list(zip(greens[0::2],greens[1::2]))


irregular=[abs(a-b) for a,b, in pairs if abs(a-b) !=42]
print(irregular)