from cv2 import cv2
import os
import face_recognition
import pymongo
from random import randint


def loadCamera():
    #Face Detection Code
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    video = cv2.VideoCapture(0)

    a = 1

    face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
    #eye_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')
    
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
                cv2.imwrite("static/images/my_image.jpg", crop_img)

    print(a) #This will print the number of frames
    video.release()
    cv2.destroyAllWindows()



    images = os.listdir('static/images')


    image_to_be_matched = face_recognition.load_image_file('static/images/my_image.jpg')


    image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]


    for image in images:
        
        current_image = face_recognition.load_image_file("static/images/" + image)
        
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
        
        result = face_recognition.compare_faces(
            [image_to_be_matched_encoded], current_image_encoded)
        
        if result[0] == True:
            print ("Matched: " + image)
            result1 = ""
            result1 = result1.join(image)
            print(result1)
            img = result1.split(".")
            print(img[0])
            break 
        else:
            print ("Not matched: " + image)


    fin = ""
    fin = fin.join(img[0])
    #print(fin) 
    return fin


    # client = pymongo.MongoClient('mongodb://localhost:27017/')
    # db = client["medical"]
    # col = db["patient_history"]  
    # #for i in col.find():
    # #   print(i)
    # from bson.objectid import ObjectId
    # [i for i in col.find({"_id": ObjectId(fin)})]