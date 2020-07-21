from PIL import Image, ImageFilter

# img = Image.open('./pokedex/bulbasaur.jpg')
# # filtered_img = img.filter(ImageFilter.BLUR)  # BLUR, SMOOTH, SHARPEN
# converted_img = img.convert('L')  # L = mode greyscale

# # print(dir(img))
# # crooked = converted_img.rotate(90)
# # resize = converted_img.resize((240, 240))
# box = (100, 100, 400, 400)
# region = converted_img.crop(box)
# # crooked.save('crooked_grey.png', 'png')
# region.save('region_grey.png', 'png')
# # crooked.show()
# region.show()
# # img
# # img.format
# # img.size
# # img.mode


img = Image.open('./astro.jpg')
# new_img = img.resize((400, 200))
# new_img.save('astro_thumbnail.jpg')
img.thumbnail((400, 200))
img.save('astro_thumbnail2.jpg')

print(img.size)
