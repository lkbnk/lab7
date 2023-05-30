from PIL import Image

watermark = "4_watermark.png"
with Image.open(watermark) as img_water: img_water.load()

img_water = Image.open(watermark)
img_water = img_water.resize((img_water.width // 2, img_water.height // 2))

filename = "4_img.png"
with Image.open(filename) as img:img.load()

img.paste(img_water, (400, 300), img_water)
img.save("4_watermark_img.png")
img.show(img_water)