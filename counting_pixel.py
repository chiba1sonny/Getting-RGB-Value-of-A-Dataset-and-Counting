from PIL import Image
import numpy as np

img = Image.open('pascal/nisgel.png').convert('RGB')
arr = np.array(img)

colours, counts = np.unique(arr.reshape(-1,3), axis=0, return_counts=1)

print(colours,counts)
