#!/usr/bin/python3
import numpy as np
import cv2 as cv
import time

# Attempt to open our default camera
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Define the codec and create VideoWriter object for our specific HW
fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame, 0)
    # write the flipped frame
    out.write(frame)
    cv.imshow('flipped frame', frame)
    #count = count + 1
    #print(count)
    #time.sleep(1)
    
    # below lines does not work with notebooks, replace it by using count
    if cv.waitKey(1) == ord('q'):
        break
    
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
