import numpy as np
import cv2
from time import *
faceCascade = cv2.CascadeClassifier('C:/Users/Kevin Polini/PycharmProjects/OpenCV/venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

video_capture =cv2.VideoCapture(0)
textAttente = ""

while(True):
    count_face=0

    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
     gray,
     scaleFactor=1.1,
     minNeighbors=5,
     minSize=(30, 30)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        count_face += 1
        seconde = count_face*20
        print ("Visage détecté : ", count_face)
        print ("temps d'attente : ",strftime('%H:%M:%S', gmtime(seconde)))
        temps_seconde =  count_face * 20
        textAttente="Temps d'attente estime a : %d s"%temps_seconde
    """ cv2.putText(frame,textAttente,(100,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)"""

    cv2.putText(frame, textAttente, (50, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (125, 0, 255), 2)
    cv2.imshow('Camera Entree',frame)

    if(cv2.waitKey(1)==ord('q')):
        break

frame.release()
cv2.destroyAllWindows()