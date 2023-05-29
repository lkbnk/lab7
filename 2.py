from PIL import Image

filename = "1_logo.jpg"
with Image.open(filename) as img:
    img.load()
img.show()

img1 = img.resize((img.width // 3, img.height // 3))
img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
img3 = img.transpose(Image.FLIP_TOP_BOTTOM)
img1.save('2_logo_v.1.jpg')
img2.save('2_logo_v.2.jpg')
img3.save('2_logo_v.3.jpg')