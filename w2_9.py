from PIL import ImageChops
import numpy as np
import PIL
from PIL import Image, ImageFilter

path = "C:/Users/bilge.adam/Downloads/ICEYE_SM_Dataset_Turkey_Syria_Earthquake_09_02_2023_1/ICEYE_SM_Dataset_Turkey_Syria_Earthquake_09_02_2023_1/"
f = "ICEYE_GRD_SM_1858459_20230209T110305.tif"

from skimage import io
img = io.imread(path + f)
print(img.shape)
img = img[10000:14300, 10000:12400]
img = img / 255.0
img = PIL.Image.fromarray(img)
img.show()