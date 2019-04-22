from PIL import Image
import os
import glob


def crop(im, height, width):

    imgwidth, imgheight = im.size
    for i in range(0, imgheight, height):
        for j in range(0, imgwidth, width):
            # print (i,j)
            box = (j, i, j + width, i + height)
            yield im.crop(box)


if __name__ == '__main__':
    path1=path="/home/anika/Documents/spl/images/gamepic/switch_1"
    path1+=".png"
    print(path1)								
    im = Image.open(path1)						
    imgwidth, imgheight = im.size
    print('Image size is: %d x %d ' % (imgwidth, imgheight))
    height = int(imgheight / 2) + 1
    width = int(imgwidth / 2) + 1
    start_num = 0

    for k, piece in enumerate(crop(im, height, width), start_num):
        #print('K: ', k, '\tpiece: ', piece)
        img = Image.new('RGB', (width, height), 255)
        img.paste(piece)
        #path = os.path.join(path +str(int(k + 1))+".png")       
        img.save(path +str(int(k + 1))+".png")
#os.rename(path, os.path.join("cam%d.1%05d" %(int(k + 1), filenum)))
