## You can use Pillow to open image files

from PIL import Image

mac = Image.open("pc.jpg")
pencil = Image.open("pencils.jpg")

# pencil.show() # This will show the image

# p_size = pencil.size # To show the size
# print(p_size)

## To crop the image
# x = 0
# y = 1100
# w = 1950/3
# h = 1300
# cropped_pencil = pencil.crop((x, y, w, h))
# cropped_pencil.show()

## To resize the image
# h, w = mac.size
# new_h = int(h/3)
# new_w = int(w/3)
# resized_mac = mac.resize((new_h,new_w))
# resized_mac.show()

## To rotate an image
# pencil.rotate(120)

