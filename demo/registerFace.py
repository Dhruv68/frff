# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:21:52 2020

@author: Dhruv
"""

from cv2 import cv2


 
def startCamera(photo_name):
      
      #Face Detection Code
      face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
      photo = ''
      video = cv2.VideoCapture(0)

      a = 1

      face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')

      while True:
            a = a + 1
            _, img = video.read()

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors=5)
            
            for x,y,w,h in faces:
                  cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255), 3)
                  
                  #eye_gray = gray[y:y+h, x:x+w]
                  #eye_color = img[y:y+h, x:x+w]
                  #eyes = eye_cascade.detectMultiScale(eye_gray)
            
            
            cv2.imshow("capture",img)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                  break
            if key & 0xFF == ord('c'):
                  crop_img = img[y: y + h, x: x + w] 
                  cv2.imwrite("static/images/" + photo_name + ".jpg", crop_img)
                  photo = crop_img

      print(a) #This will print the number of frames
      video.release()
      cv2.destroyAllWindows()
      return photo