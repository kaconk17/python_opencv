import cv2
import numpy as np
import face_recognition
import pickle


with open('encoded_face.dat','rb') as extfile:
    allface_data = pickle.load(extfile)

    
classnames = list(allface_data.keys())
listknown = np.array(list(allface_data.values()))


cap = cv2.VideoCapture(0)
scale = 100
accurate = 0
print(classnames)
while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    facescurframe = face_recognition.face_locations(imgS)
    encodecurframe = face_recognition.face_encodings(imgS,facescurframe)

    for encodeface, faceloc in zip(encodecurframe, facescurframe):
        matches = face_recognition.compare_faces(listknown, encodeface)
        facedis = face_recognition.face_distance(listknown, encodeface)
        
        matchindex = np.argmin(facedis)
        if matches[matchindex]:
            accurate = accurate + 1
            name = classnames[matchindex].upper()
            y1,x2,y2,x1 = faceloc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img, (x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img, (x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            if accurate == 20:
                crop_img = img[y1-scale:y2+scale, x1-scale:x2+scale]
                accurate = 0
                cv2.destroyWindow('Camera')
                cv2.imshow("OK",crop_img)
                cv2.waitKey(2000)



    cv2.imshow('Camera', img)
    cv2.waitKey(1)
