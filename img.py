from PIL import Image
import glob, os

size = 256, 256
#path=str(os.path.abspath(os.path.join(os.path.dirname(__file__),"infile")))
path="/home/rajiv/Music/infile/*.jpeg"
outpath = "/home/rajiv/Music/outfile/"
print path
files=glob.glob(path)   
for file in files:    
#for file in path:
    
    img = Image.open(file)
    print file
  
    img = img.resize((100,100), Image.ANTIALIAS)
    
    img=img.save(os.path.join(os.path.dirname(__file__),"outfile"),"JPEG")
    
  
    
    
    
