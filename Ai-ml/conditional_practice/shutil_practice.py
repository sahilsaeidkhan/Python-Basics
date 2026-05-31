import os
import shutil 

if not os.path.exists("Images"):
    os.mkdir("Images")

shutil.move("photo.jpg","Images")