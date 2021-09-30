from pathlib import Path
from PIL import Image

PADDING = -2

for boxfile in Path('.').rglob('*.box'):
    x1_all, y1_all, x2_all, y2_all = [], [], [], []
    with open(boxfile, 'r') as fin:
        for line in fin.readlines():
            if len(line.split(' ')) > 4:
                x1, y1, x2, y2, _ = line.replace('  ',' ').split(' ')[1:]
                x1_all.append(int(x1))
                y1_all.append(int(y1))
                x2_all.append(int(x2))
                y2_all.append(int(y2))
    img = Image.open(str(boxfile.with_suffix('.tif').resolve()))
    box = (min(x1_all)-PADDING, min(y1_all)-PADDING, max(x2_all)+PADDING, max(y2_all)+PADDING)
    cropped_img = img.crop(box)
    cropped_img.save(boxfile.with_suffix('.png'))