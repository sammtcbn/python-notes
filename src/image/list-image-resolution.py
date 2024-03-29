# pip install pillow
from PIL import Image
from pathlib import Path

home_dir = Path.home()

target_dir = home_dir / 'Pictures'

for picpath in target_dir.glob('*.jpg'):
    img = Image.open(picpath)
    print(f'{picpath} {img.width}x{img.height}')
