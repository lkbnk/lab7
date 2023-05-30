from PIL import Image, ImageFilter

filename = ["3_img1.jpg", "3_img2.jpg", "3_img3.jpg", "3_img4.jpg", "3_img5.jpg"]
for i in filename:
    with Image.open(i) as img:
        img.load()
        new_img = img.filter(ImageFilter.FIND_EDGES)
        new_img.save("NEW_"+i)
        new_img.show()