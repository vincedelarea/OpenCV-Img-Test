import cv2 as cv
import numpy as np

file = './klee.png'
img = cv.imread(file)

if(len(img.shape)<3):
    raiden = cv.imread('./raiden_pout.png')
    cv.imshow("I don't accept Greyscale images. o(>=<)o", raiden)
    cv.waitKey(0)
    cv.destroyAllWindows()
elif(len(img.shape)==3):
    print("Loading " + file + "...")
    cv.imshow("cute", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print("SHOW SPECIFIC PIXEL IN IMAGE")
    inputX = int(input("X:"))
    inputY = int(input("Y:")) 
    channel = int(input("Color Channel 0-BLUE, 1-GREEN, 2-RED\nChannel:"))
    print(img.item(inputX, inputY, channel))
    print("MODIFY PIXEL VALUE IN IMAGE")
    blue = input("Blue Channel Value (0-255):")
    green = input("Green Channel Value (0-255):")
    red = input("Red Channel Value (0-255):")
    print("BEFORE: ", img[inputX, inputY])
    img.itemset((inputX, inputY, 0), blue)
    img.itemset((inputX, inputY, 1), green)
    img.itemset((inputX, inputY, 2), red)
    print("AFTER: ", img[inputX, inputY])
    kleeDimension = img.shape
    fixDimension = (720, 700, 3)
    if(kleeDimension[0]>=fixDimension[0] and kleeDimension[1]>=fixDimension[1]):
        print("Inside of Klee's Territory. \(★ω★)/")
    else:
        print("Outside of Klee's Territory. (ᗒᗣᗕ)՞")
    size = img.size
    fixSize = 2764799
    if(size>fixSize):
        print("The set pixel is lower than Image total pixel count.")
    else:
        print("The set pixel is higher than Image total pixel count.")
    print("Loaded Image data type: ", img.dtype)