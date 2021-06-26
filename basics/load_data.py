import PIL
import tensorflow as tf

import pathlib

data_dir = pathlib.Path("../data/flower_photos")
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

roses = list(data_dir.glob('roses/*'))
PIL.Image.open(str(roses[0]))

