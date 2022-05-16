import cv2
import os
import imutils

nombreRostro = 'Melissa'
guardado = 'D:\Angel\FCA\Inteligencia Artificial\ProyectoIA\caras'
rostroGuardado = guardado + '/' + nombreRostro

if not os.path.exists(rostroGuardado):
    print('Nueva carpeta creada: ',rostroGuardado)
    os.makedirs(rostroGuardado)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count = 0

cap = cv2.VideoCapture('melissa.mp4')

while True:
    ret, img = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rostro = face_cascade.detectMultiScale(gray, 1.1, 4)
    auxFrame = img.copy()
    for (x, y, w, h) in rostro:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 150), 2)
        rostro = auxFrame[y:y+h,x:x+h]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        cv2.imwrite(rostroGuardado + '/rostro_{}.jpg'.format(count),rostro)
        count = count + 1
    cv2.imshow('img', img)

    k = cv2.waitKey(30)
    if k == 27 or count >= 300:
        break
cap.release()