#we can run camera through our webcam using python
import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
  #Capture the video frame by frame
  ret, frame = video.read()
  
  cv2.imshow('frame', frame)

video.release()
cv2.destroyAllWindows() 
