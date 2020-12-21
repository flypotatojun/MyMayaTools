from PIL import Image
import sys
import os

# path = 'E:\\pythonProject\\MyMayaTools\\myPlugins\\scripts\\BlueLineGame\\test\\'
path = 'E:\\pythonProject\\MyMayaTools\\myPlugins\\scripts\\BlueLineGame\\'


# for i in os.listdir(path):
#     # fullpath = os.path.join(path, i)
#     # if os.path.isfile(fullpath):
#     listFile = os.path.splitext('.')[1]=='.png'

# listFile = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.png']
listFile = [x for x in os.listdir(path) if os.path.isfile(x) and os.path.splitext(x)[1]=='.png']

listFile.sort()

new_image = Image.new('RGBA', (720, 1280))
for file in listFile:

    FileNum = file.split('.')[1][-4:]
    CropLine = int((int(FileNum)-1000)*6.46)

    im = Image.open(path + file)
    r, g, b, a = im.split()

    box = (0, CropLine, 720, CropLine+7)
    
    im_crop = im.crop(box)
    r, g, b, a = im_crop.split()


    i = 1
    for y in range(len(listFile)):
        i+=1
        print(i)
    comp_image = Image.composite(im_crop, im_crop, a )
    new_image.paste(comp_image, box)


new_image.save(path + 'comp.tif')

new_image.show()
