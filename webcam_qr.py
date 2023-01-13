# -*- coding: UTF-8 -*-
#Paradigmas Tecnologicos II - Robotica 2020 Universidad Abierta Interamericana
#Ing Nestor Adrian Balich
#este material es GNU captura imagenes con pyOpenCV
#reconoce codigos QR cpn pyzbar
import sys
import cv2
import numpy as np
from pyzbar.pyzbar import decode   # pip install zbar

#----------------- captura de imagen    
cam1 = cv2.VideoCapture(0)

cam1.set(3, 640)
cam1.set(4, 480)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 95]

sin_qr = 0

print("Presione o para salir del programa")

while (cam1.isOpened()):
   ret, frame = cam1.read()

 # detecta codigo qr cuando no reproduce video
   for barcode in decode(frame):
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(frame,[pts],True,(0,0, 255),2)
        pts2 = barcode.rect
        cv2.putText(frame,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),1)

   cv2.imshow('Webcam reconociendo QR', frame)	

   #sale del programa con "s"	   		
   if cv2.waitKey(1) & 0xFF == ord('o'):
	   break

cam1.release()
cv2.destroyAllWindows()

