# import libraries
import cv2
import numpy as num
import face_recognition
import os

path = 'Image_Attendance'
images = []
Names = []
myList = os.listdir(path)

Elonimg = face_recognition.load_image_file('Images/Elon1.jpg')
Elonimg = cv2.cvtColor(Elonimg,cv2.COLOR_BGR2RGB)
Elonimg2 = face_recognition.load_image_file('Images/Elon2.jpg')
Elonimg2 = cv2.cvtColor(Elonimg2,cv2.COLOR_BGR2RGB)

face_location = face_recognition.face_locations(Elonimg)[0]
Elon_encode = face_recognition.face_encodings(Elonimg)[0]
cv2.rectangle(Elonimg,(face_location[3],face_location[0]), (face_location[1],face_location[2]), (255,0,255),2)

face_location2 = face_recognition.face_locations(Elonimg2)[0]
Elon_encode2 = face_recognition.face_encodings(Elonimg2)[0]
cv2.rectangle(Elonimg2,(face_location2[3],face_location2[0]), (face_location2[1],face_location2[2]), (255,0,255),2)

results = face_recognition.compare_faces([Elon_encode],Elon_encode2)
face_distance1 = face_recognition.face_distance([Elon_encode],Elon_encode2)
print(results,face_distance1)
print(results)

cv2.putText(Elonimg2,f'{results} {round(face_distance1[0],2)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)



cv2.imshow('Elon_Musk',Elonimg)
cv2.imshow('Elon_Musk2',Elonimg2)
cv2.waitKey(0)