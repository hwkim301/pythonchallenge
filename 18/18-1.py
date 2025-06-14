import difflib
import gzip 

d1,d2=[],[]

with gzip.open("deltas.gz","rb") as f:
    for line in f:
        d1.append(line[:53].decode("utf-8")+"\n")
        d2.append(line[56:].decode("utf-8"))


for diff in difflib.Differ().compare(d1,d2):
    print(diff)


with (
    open("f1","wb") as f1,
    open("f2","wb") as f2,
    open("f3","wb") as f3
):
   
   for difference in difflib.Differ().compare(d1,d2):
       data=bytes.fromhex("".join(difference[2:].strip("").split(" ")))
       if difference.startswith("-"):
           f1.write(data)
       
       elif difference.startswith("+"):
           f2.write(data)
        
       else:
           f3.write(data)