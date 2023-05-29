from PIL import Image

water = "4_img.png"
with Image.open(water) as img_water: img_water.load()

img_water = Image.open(water).convert('RGBA')
img_water = img_water.resize((img_water.width // 10, img_water.height // 10))

filename = "1_logo.jpg"
with Image.open(filename) as img: img.load()

img.paste(img_water, (300,350),img_water)
img.save("4_watermark_img.png")