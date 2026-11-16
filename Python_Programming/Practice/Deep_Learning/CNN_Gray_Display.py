from PIL import Image
import numpy as np

img = Image.open("digit_28x28.png")
print(img.size)

#  L LETTER IS USED TO CONVERT THE IMAGE INTO Grey Scale
img = img.convert("L")
img = img.resize((28,28))

pixels = np.array(img)

print("Image size : ",pixels.shape)

print("Pixel values : ")
print(pixels)

# 0     Pure Black
# 255   Pure White
# 50    Dark Gray
# 120   Medium Gray
# 200   Light Gray