import cv2 as cv
import numpy as np

PATH = 'image.jpeg'
def sobel_function():
    image = cv.imread(PATH)
    kernelX =  np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernelY =  np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

    sobelX =   cv.Sobel(image,cv.CV_64F,1,0)

    sobelY =   cv.Sobel(image,cv.CV_64F,0,1)

    Hori = np.concatenate((sobelX, sobelY), axis=1)
    cv.imshow("SOBEL", Hori)
    cv.waitKey(0)
    cv.destroyAllWindows()


sobel_function()

