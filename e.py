import os

from PIL import Image
import numpy as np

base = '1'
all_image = os.listdir(base)
result = []
for img in all_image:
    image = Image.open(f'{base}/{img}').convert('RGB')
    na = np.array(image)
    colors = na.reshape(-1, 3)
    result.extend(colors)
    colors = np.unique(result, axis=0, return_counts=1)
    result = colors[0].tolist()
print(result)