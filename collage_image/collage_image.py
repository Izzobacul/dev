#!./env/bin/python

from PIL import Image
import requests

url = 'https://picsum.photos/200/200'

img_path = input("Enter the input image path: ")
start = Image.open(img_path)
size = start.size
images = [[None for x in range(20)] for i in range(20)]
out = Image.new('RGB', (size[0], size[1]))
im_size = size[0] // 20
for i in range(20):
    for j in range(20):
        img = Image.open(requests.get(url, stream=True).raw)
        img = img.resize((im_size, im_size))
        out.paste(img, (i*20, j*20))
        print(f"Image {i*20 + j}")
out.show()
# url = 'https://picsum.photos/500/500'
# im1 = Image.open(requests.get(url, stream=True).raw)
# # im2 = Image.open(requests.get(url, stream=True).raw)
# # collage = Image.new('RGB', (2*im1.size[0], im1.size[1]), (250, 250, 250))
# # collage.paste(im1, (0, 0))
# # collage.paste(im2, (im1.size[0], 0))
# # collage.save('collage.jpg')
# # collage.show()
#
# im1 = im1.resize((200, 200))
# im1.save('1x1.jpg')
# print(im1.pixel(0, 0))
