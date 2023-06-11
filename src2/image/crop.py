# pip install Pillow
from PIL import Image
from pathlib import Path

target_jpg = Path('picture.jpg')
img = Image.open(target_jpg)
newimg = img.crop((0, 100, 800, 800))
newimg.show()
newimg.save('picture_crop.jpg')
