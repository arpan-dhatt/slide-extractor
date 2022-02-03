import cv2
import math

vidPath = 'media/videos/cs429.mp4'
imPath = 'media/cvOutput'

cap = cv2.VideoCapture(vidPath)
frameRate = cap.get(5)

while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = imPath + "/image_" +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, frame)
cap.release()
print("DONE")