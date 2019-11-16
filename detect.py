# import the necessary packages
# from imutils import paths
import numpy as np
# import argparse
# import imutils
# import pickle
import cv2
import os
import requests
# import scikit-learn ## matching people


cap = cv2.VideoCapture(0)

while True:
   # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
