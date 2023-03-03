from matplotlib import cm
from PIL import ImageChops
import numpy as np
import PIL
from PIL import Image, ImageFilter

# Open the image form working directory
image = Image.open("C:/Users/bilge.adam/Desktop/test.png")
image = image.convert('L')
original = image
# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)
# show the image

sobel = image.filter(ImageFilter.FIND_EDGES)
sobelmean = np.mean(sobel)

sobel2 = sobel > np.quantile(sobel, 0.95)
#sobel2 = Image.fromarray(np.uint8(cm.gist_earth(sobel2)*255))
sobel2 = PIL.Image.fromarray(sobel2)

rgbimg = Image.new("RGBA", sobel2.size)
rgbimg.paste(sobel2)
sobel2 = rgbimg

sobel2 = sobel2.filter(ImageFilter.GaussianBlur)
sobel2 = sobel2.filter(ImageFilter.GaussianBlur)


blur = image.filter(ImageFilter.BLUR)


image = ImageChops.difference(blur, image)
image = image.filter(ImageFilter.BLUR)


image = original.filter(ImageFilter.SHARPEN)

sobel2.show()