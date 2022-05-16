import cv2
import os
import numpy as np

guardado = 'D:\Angel\FCA\Inteligencia Artificial\ProyectoIA\caras'
personas = os.listdir(guardado)
print('Lista de personas: ', personas)

labels = []
facesData = []
label = 0

for personaDir in personas:
    personaGuardado = guardado + '/' + personaDir
    print('Leyendo imagenes')

    for fileName in os.listdir(personaGuardado):
        print('Rostros: ', personaDir + '/' + fileName)
        labels. append(label)
        facesData.append(cv2.imread(personaGuardado+'/'+fileName,0))
        image = cv2.imread(personaGuardado+'/'+fileName,0)
        #cv2.imshow('image',image)
        #cv2.waitKey(10)
    label = label + 1

reconocimiento = cv2.face.EigenFaceRecognizer_create()

print("Entrenamiento")
reconocimiento.train(facesData, np.array(labels))

print("Almacenando Modelo")
reconocimiento.write('modelosRostros.xml')
print("Modelo almacenado")
