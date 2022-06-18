''''
Capture multiple Faces from multiple users to be stored on a DataBase (dataset directory)
	==> Faces will be stored on a directory: dataset/ (if does not exist, pls create one)
	==> Each face will have a unique numeric integer ID as 1, 2, 3, etc                       

Based on original code by Marcelo Rovai: https://github.com/Jacob12138xieyuan/easy-real-time-face-recognition-python    

Developed by Haruki Konii
'''

import cv2
import os
import sys


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')
start_count = int(input('\n enter start_count and press <return> ==>  '))    # default = 1, starts from User.X.start_count.jpg

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

cam = cv2.VideoCapture(0) # 0 means default camera attached on your PC
if cam.isOpened() is False:
    print("can not open camera")
    sys.exit()

cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

while(True):
    ret, img = cam.read()   # get 1 frame from default cam
    #if flame is not obtained, close
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    cv2.imshow("image", img)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        print("face's count:", count)
        
        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(start_count) + ".jpg", gray[y:y+h,x:x+w])
        start_count += 1

        cv2.imshow('image', img)    #show a current video 

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()