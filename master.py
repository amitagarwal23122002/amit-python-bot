#we can run camera through our webcam using python
import cv2
import numpy as np

video_address = "" # Input Your IP WEBCAM IP address here
video = cv2.VideoCapture(video_address)

while True:
  #Capture the video frame by frame
  ret, frame = video.read()
  
  cv2.imshow('frame', frame)

video.release()
cv2.destroyAllWindows() 
