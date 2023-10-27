# pip install pillow
from PIL import Image
from pathlib import Path

target_jpg = Path('target.jpg')
img = Image.open(target_jpg)
img.show()

