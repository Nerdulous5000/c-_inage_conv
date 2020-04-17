# Pyton 3.8.2
import cv2 
import sys
import re

fileName = "it_stripes.png"
fileName = sys.argv[1]
separetedFileName = re.split(r'[\\/]', fileName) 
print(separetedFileName)
dispName = separetedFileName[-1]
print("Test")
img = cv2.imread(fileName)
cv2.imshow('image', img)  
imgSize = img.shape

f = open("output.txt", "w")
f.write("// Filename: %s\n" % dispName)
f.write("// File generated to display an image by columns in the format:")
f.write("// [red, green, blue,]\n")
f.write("char tempTex[] = {")

# BGR Color format
for n in range(imgSize[0]):
    for i in range(imgSize[1]):
        pixel = img[i, n]
        #outputs 0xred, 0xblue, 0xgreen,
        f.write("%s, %s, %s,\n" % (hex(pixel[2]), hex(pixel[1]), hex(pixel[0])))
        # print(pixel)
    # print("")
f.write("};")
f.close()