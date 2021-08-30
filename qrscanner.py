from imutils.video import VideoStream, videostream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import requestbooking
import numpy as np

vs  = VideoStream(src=0).start()

time.sleep(2)

while True:
    
    frame = vs.read()
    frame = imutils.resize(frame,width=400)

    barcodes = pyzbar.decode(frame)

    data = None

    for bar in barcodes:
        

        pts = np.array([bar.polygon],np.int32)
        pts = pts.reshape((-1,1,2))

        cv2.polylines(frame,[pts],True,(255,0,255),5)

        data = bar.data.decode('utf-8')

    FlippedImage = cv2.flip(frame, 1)

    cv2.imshow("QRCode scanner",FlippedImage)

    if data is None:
        pass
    else:
                    
        statuscode,num = requestbooking.req_code(data)

        if str(statuscode) == "200":
            print(num)
            stscode = requestbooking.check(str(num))
            print(stscode)
        else:
            print(statuscode)
            print("RED LIGHT")

        data = None
        time.sleep(2)


    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break