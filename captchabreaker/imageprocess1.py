from PIL import Image
import numpy as np

HIGHESTLEVEL = 7
image127 = Image.open('OCRTemp6.png')
image170 = Image.open('OCRTemp4.png')

image127_data = np.asarray(image127)
image170_data = np.asarray(image170)
image170_data_tobe = np.asarray(image170)
image170_data_tobe.setflags(write=1)
for i in range(len(image127_data)):
    for j in range(len(image127_data[0])):
        xpixel=i+2*HIGHESTLEVEL
        ypixel=j+2*HIGHESTLEVEL
        if(xpixel>=0 and xpixel<len(image127_data) and ypixel>=0 and ypixel<len(image127_data[0])):
            if(image170_data[xpixel][ypixel]==0):
                for x in range((xpixel - HIGHESTLEVEL), (xpixel + HIGHESTLEVEL)):
                    for y in range((ypixel - HIGHESTLEVEL), (ypixel + HIGHESTLEVEL)):
                        if(x>=0 and x<len(image127_data) and y>=0 and y<len(image127_data[0])):
                            if(image170_data[x][y]==255 and image127_data[x][y]==0):
                                image170_data_tobe[x][y]=0
                                #print(image170_data[x][y])
            
#print(image127_data[182][538])
#print(image170_data[182][538])
imgfinal = Image.fromarray(image170_data_tobe)
imgfinal.save('OCRTemp7.png')
