from PIL import Image
from PIL import ImageDraw

img = Image.open('pictures file')
img_draw= ImageDraw.Draw(img)
img_draw.text((28, 36), "Hi", fill=(255, 0,0))
img.save('pictures file')

