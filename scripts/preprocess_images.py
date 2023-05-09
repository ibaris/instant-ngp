from PIL import Image
import os

path = "C:\\Users\\sche_m17\\Documents\\git\\instant-ngp\\data\\nerf\\TM03-1_AABB_2\\images"

for filename in os.listdir(path):

    if filename.endswith(".jpg") or filename.endswith(".png"):
    
        with Image.open(os.path.join(path, filename)) as im:
        
            new_filename = filename.replace("(", "").replace(")", "").replace(" ", "")
           
            im.convert("RGB").save(os.path.join(path, new_filename), "JPEG")
            
            #Hier musste ich einfach ein bisschen mit den Parametern rumspielen dann hats gepasst
            width, height = im.size
            left = (width - 1270) // 2
            top = (height - 700) // 2
            right = left + 1270
            bottom = top + 700
            new_im = im.crop((left, top, right, bottom))

            new_im.save(os.path.join(path, new_filename), "JPEG")
