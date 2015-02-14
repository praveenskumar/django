import os,sys
from PIL import Image

path1 = os.path.abspath(os.path.join("infile"))
path2 = os.path.abspath(os.path.join("outfile"))
print path2
count=0
for file in os.listdir(path1):
    count+=1
    current = os.path.join(path1, file)
    if os.path.isfile(current):         
        img = Image.open(current)
        img.resize((100,100), Image.ANTIALIAS)
        img.save(path2+"/"+str(count)+".jpeg",quality=100)
