from PIL import Image

def bilde():

  datne = "15.11/bildite.JPG"

  with Image.open(datne) as im:
    print(datne, im.format, f"{im.size}x{im.mode}")
    im.show()
    izmers = (100,100)
    im.thumbnail(izmers)
    im.save("15.11/maza_bilde.jpg", im.format)
    im.show()

bilde()


from PIL import Image

im = Image.open("sample-image.png")
angle = 90
out = im.rotate(angle)
out.save('rotate-output.png')