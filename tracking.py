# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 20:09:16 2023

@author: Jenci
"""

import cv2

tracker = cv2.legacy.TrackerMOSSE_create()

cap = cv2.VideoCapture(0)
bbox = None

def drawBox(img,bbox,centerx,centery):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    targetx = (x + int(w//2)) - centerx
    targety = (y + int(h//2)) - centery
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (0, 0, 255), 3, 3 )
    cv2.putText(img, "Tracking X=       Y=", (80, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(img, str(targetx), (180, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(img, str(targety), (260, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    

while True:
    timer = cv2.getTickCount()
    success, img = cap.read()
    centerx = img.shape[1]//2
    centery = img.shape[0]//2
    img_clean = img.copy()
    
    if bbox is not None:
        success, bbox = tracker.update(img_clean)
        if success:
            drawBox(img,bbox,centerx,centery)
            print("action")
        else:
            cv2.putText(img, "Lost", (80, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    cv2.putText(img, "FPS:", (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2);
    cv2.putText(img, "Status:", (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2);
    cv2.line(img, (centerx, centery), (centerx, centery+50), (255,255,0), 2);
    cv2.line(img, (centerx-20, centery), (centerx-80, centery), (255,255,0), 2);
    cv2.line(img, (centerx+20, centery), (centerx+80, centery), (255,255,0), 2);

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    if fps>60:
        myColor = (0,255,0)
    elif fps>20:
        myColor = (255,0,0)
    else:
        myColor = (0,0,255)
    cv2.putText(img,str(int(fps)), (65, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, myColor, 2);

    cv2.imshow("Tracking", img)
    if cv2.waitKey(10) & 0xff == ord('s'):
        bbox = cv2.selectROI("Tracking", img, fromCenter=False, showCrosshair=False)
        tracker.init(img, bbox)
    
    if cv2.waitKey(10) & 0xff == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()
