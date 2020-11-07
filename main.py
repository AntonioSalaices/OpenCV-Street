# Importamos las librerías necesarias
import numpy as np
import cv2
import time

captura = cv2.VideoCapture(0)
while (captura.isOpened()):
  ret, imagen = captura.read()
  gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
  
  if ret == True:
    rectangle = cv2.rectangle(imagen, (80,100),(100,-100), (0,255,0), 10)
    cv2.imshow('video', imagen)
    cv2.imshow('video a escala de grises', gris)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
captura.release()
cv2.destroyAllWindows()
