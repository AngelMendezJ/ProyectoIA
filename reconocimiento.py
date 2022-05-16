import cv2
import os
from hmac import trans_36
from unittest import result
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser
import pyautogui
import time
import pyautogui

xi = 1
guardado = 'D:\Angel\FCA\Inteligencia Artificial\ProyectoIA\caras'
rostrosGuadados = os.listdir(guardado)
print('rostrosGuardados=', rostrosGuadados)

reconocimiento = cv2.face.EigenFaceRecognizer_create()

reconocimiento.read('modelosRostros.xml')

cap = cv2.VideoCapture('melissa.mp4')

clasificarRostro = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret, img = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()
    
    rostros = clasificarRostro.detectMultiScale(gray ,1.1, 4)

    for (x,y,w,h) in rostros:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        result = reconocimiento.predict(rostro)

        cv2.putText(img,'{}'.format(result),(x,y-5),1,1.3,(255,0,150),1,cv2.LINE_AA)
        
        if result[1] < 3000:
            cv2.putText(img,'{}'.format(rostrosGuadados[result[0]]),(x,y-25),1,1.3,(255,0,150),1,cv2.LINE_AA)
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 150), 2)

            if xi <= 1:
                
                xi = xi + 1
                client_id = "5ef6339bf8424873900df12dc10e3b62"
                client_secret = "7321cb422d0549488410ed879b7bd040"
                author = 'Odyssey'
                song = "Resonance"

                sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
                result = sp.search(author)

                for i in range(0, len(result["tracks"]["items"])):
                    name_song = result["tracks"]["items"][i]["name"]
                    if song == name_song:
                        webbrowser.open(result["tracks"]["items"][i]["uri"])
                
                pyautogui.click(1450, 600)
                pyautogui.moveTo(1210, 50)  

            else:
                break

        else:
            cv2.putText(img,"Rostro no almacenado",(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('frame',img)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()