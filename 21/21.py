import zlib
import bz2


with open("package.pack", "rb") as f:
    content = f.read()

copper=""
while True:
    try:
        data = zlib.decompress(content)
        content = data
        copper+=" "
    except zlib.error:
        try:
            data = bz2.decompress(content)
            content = data
            copper+="#"
        except OSError:
            try:
                data = zlib.decompress(content[::-1])
                content = data
                copper+="\n"
            except zlib.error:
                try:
                    data = bz2.decompress(content[::-1])
                    content = data
                except OSError:
                    break

print(copper)