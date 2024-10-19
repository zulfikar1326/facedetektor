import cv2 as cv
import numpy


kamera = cv.VideoCapture(0)


if not kamera:
    print("Kamera Tidak ada")
    exit('Program Berakhir')

while True:
    
    ret, frame = kamera.read()

    if ret == False:
        print('KEsalahan System') 
        
    addcolor = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow("camera",addcolor)
    
    if cv.waitKey(1) == ord('x'):
        cv.destroyAllWindows()
        break
    