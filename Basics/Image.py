from PIL import Image

img = Image.open('pic1.jpg')
img_copy = img.copy()
cropped_image = img.crop((265, 345,565,560))
img_copy.paste(cropped_image, (0,0))
img_copy.save('cropped_pic1.jpg')
