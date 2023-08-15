#remove background from image 
'''
Requirements=>
PIL=> pip install pillow 
rembg => pip install rembg 
'''

from PIL import Image 
from rembg import remove 

image = Image.open("Limage.jpg")
out  = remove(image)
out.save("bgrem.png")
