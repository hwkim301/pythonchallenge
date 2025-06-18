import zlib
import bz2


with open("package.pack", "rb") as f:
    content = f.read()

logs=""

while True:
    try:
        data = zlib.decompress(content)
        content = data
        print("z",end=" ")
    except zlib.error:
        try:
            data = bz2.decompress(content)
            content = data
            print("b",end=" ")
        except OSError:
            try:
                data = zlib.decompress(content[::-1])
                content = data
                print("r",end=" ")
            except zlib.error:
                try:
                    data = bz2.decompress(content[::-1])
                    content = data
                except OSError:
                    break

