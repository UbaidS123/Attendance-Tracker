import cv2
import numpy as num
import face_recognition



Elonimg = face_recognition.load_image_file('Images/Elon1.jpg')
Elonimg = cv2.cvtColor(Elonimg,cv2.COLOR_BGR2RGB)
Elonimg2 = face_recognition.load_image_file('Images/Elon2.jpg')
Elonimg2 = cv2.cvtColor(Elonimg2,cv2.COLOR_BGR2RGB)

