import cv2
import numpy as np
import face_recognition
import os
import pickle

pathfoto = "foto"
cap = cv2.VideoCapture(0)
scale = 100



def save_encode(gambar, name, path):
    allface_data = []
    imgS = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)
    facescurframe = face_recognition.face_locations(imgS)
    encodecurframe = face_recognition.face_encodings(imgS,facescurframe)[0]
    name = name.upper()

    if os.path.exists('encoded_face.dat'):
        with open('encoded_face.dat','rb') as extfile:
            allface_data = pickle.load(extfile)
            face_name = list(allface_data[0].keys())
            face_encoding = np.array(list(allface_data[0].values()))
    else:
        face_name = []

    if name not in face_name:
        cv2.imwrite(f'{path}/{name}.png', gambar)
        newdata[name] = encodecurframe
        allface_data.append(newdata)
        with open('encoded_face.dat','wb') as f:
            pickle.dump(allface_data,f)
        print('Save Face data success')
    else:
        print('Nama sudah terdaftar !')
    

while True:
    success, img = cap.read()
    if not success:
        print("Gagal aktivasi Camera")
        break
    k = cv2.waitKey(1)
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    facelocframe = face_recognition.face_locations(imgS)

    for faceloc in facelocframe:
        top, right, bottom, left = faceloc
        top, right, bottom, left = top*4, right*4, bottom*4, left*4
        if k%256 == 27:
            print("Tutup aplikasi....")
            break
        elif k%256 == 32:
            crop_img = img[top-scale:bottom+scale, left-scale:right+scale]
            cv2.imshow("croped",crop_img)
            cv2.waitKey(0)
            name = input("masukkan nama :")
            
            save_encode(crop_img, name, pathfoto)
            
    
        cv2.rectangle(img,(faceloc[3]*4,faceloc[0]*4),(faceloc[1]*4,faceloc[2]*4),(0,255,0),2)

    cv2.imshow('Camera', img)
    cv2.waitKey(1)



    