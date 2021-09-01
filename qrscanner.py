from os import error
from imutils.video import VideoStream, videostream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import requestbooking
import numpy as np
from win32api import GetSystemMetrics

#try except causes more lag

try :
    vs  = VideoStream(src=0).start()

    time.sleep(2)

    Width =GetSystemMetrics(0)
    Height =GetSystemMetrics(1)
except:
    print("camera error")


while True:
    
    frame = vs.read()
    frame = imutils.resize(frame,width=Width,height=Height)

    barcodes = pyzbar.decode(frame)

    data = None
    
    

    for bar in barcodes:
        

        pts = np.array([bar.polygon],np.int32)
        pts = pts.reshape((-1,1,2))

        cv2.polylines(frame,[pts],True,(255,0,255),5)

        data = bar.data.decode('utf-8')

    FlippedImage = cv2.flip(frame, 1)
    cv2.namedWindow("QRCode scanner")
    cv2.moveWindow("QRCode scanner",0,0)
    cv2.imshow("QRCode scanner",FlippedImage)

    if data is None:
        pass
    else:
        try:          
            statuscode,num = requestbooking.req_code(data)

            if str(statuscode) == "200":
                print(num)
                stscode = requestbooking.check(str(num))
                print(stscode)
                pass_img = cv2.putText(FlippedImage,"Booking Found",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
                cv2.imshow("QRCode scanner",pass_img)
                cv2.waitKey(5000)
            else:
                print(statuscode)
                fail_img = cv2.putText(FlippedImage,"Booking Not Found",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                cv2.imshow("QRCode scanner",fail_img)
                cv2.waitKey(1000)

            data = None

        except:
            #print("connection error")
            msg = "Connection Error"
            error_img = cv2.putText(FlippedImage,msg,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
            cv2.imshow("QRCode scanner",error_img)
            cv2.waitKey(3)


    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break