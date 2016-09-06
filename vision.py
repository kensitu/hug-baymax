import cv2
import sys
import numpy as np
import serial

#Set up variables
upperBodyCascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
webcamCapture = cv2.VideoCapture(0)
width = 640
height = 360
numPixels = width * height
thresholdFrac = .5
oldBool = False
currentBool = False
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

while True:
    # Capture frame by frame
    ret, frame = webcamCapture.read()

    # Convert images to smaller size
    frame = cv2.resize(src = frame, 
                dst = frame, 
                dsize = (width, height), 
                fx = 0, 
                fy = 0, 
                interpolation = cv2.INTER_AREA
                )

    # Convert images to grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert images to black/white
    ret, frame = cv2.threshold(frame, 110, 255, cv2.THRESH_BINARY)

    # Count non-zero (white) pixels
    numWhite = cv2.countNonZero(frame)
    numBlack = numPixels - numWhite

    # Check pixels against our threshold
    oldBool = currentBool
    currentBool = numBlack > (numPixels * thresholdFrac)
    
    if (currentBool and not oldBool):
        #START THE HUG
	   ser.write('1');                 #send a Serial command to hug
    if (not currentBool and oldBool):
        #END THE HUG            
	   ser.write('2');                 #send a Serial command to end hug

    # These next two lines bring up a window that graphically shows what the webcam is seeing.
    # To boost performance, comment out the next two lines.
    cv2.namedWindow("", cv2.WINDOW_NORMAL)
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

webcamCapture.release()
