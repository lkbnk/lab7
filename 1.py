from PIL import Image

filename = "1_logo.jpg"
with Image.open(filename) as img:
    img.load()
img.show()

print("Ширина: ", img.size[0], "пикселей")
print("Высота:  ", img.size[1], "пикселей")
print("Цветовая модель:", img.mode)
print("Формат: ", img.format)