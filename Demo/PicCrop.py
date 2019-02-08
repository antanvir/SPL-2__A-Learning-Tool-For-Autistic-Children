from PIL import Image
import os
import glob


def crop(im, height, width):
    # im = Image.open(infile)
    imgwidth, imgheight = im.size
    for i in range(0, imgheight, height):
        for j in range(0, imgwidth, width):
            # print (i,j)
            box = (j, i, j + width, i + height)
            yield im.crop(box)


if __name__ == '__main__':
    '''
    # change the path and the base name of the image files
    imgdir = 'Pictures'
    basename = 'img-*.tif'
    filelist = glob.glob(os.path.join(imgdir, basename))
    for filenum, infile in enumerate(filelist):
        # infile='/Users/alex/Documents/PTV/test_splitter/cal/Camera 1-1-9.tif'
        print (filenum)  # keep the numbers as we change them here
        print (infile)
    '''
    im = Image.open("mango.jpg")
    imgwidth, imgheight = im.size
    print ('Image size is: %d x %d ' % (imgwidth, imgheight))
    height = int(imgheight / 2) + 1
    width = int(imgwidth / 2) + 1
    start_num = 0
    for k, piece in enumerate(crop(im, height, width), start_num):
            # print k
            # print piece
        print('K: ', k, '\tpiece: ', piece)
        #print(width, "\t", height)
        img = Image.new('RGB', (width, height), 255)
            # print img
        img.paste(piece)
        path = os.path.join("IMG-%d.jpg" % int(k + 1))
        img.save(path)
        #os.rename(path, os.path.join("cam%d.1%05d" %(int(k + 1), filenum)))
