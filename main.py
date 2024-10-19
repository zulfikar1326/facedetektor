import cv2 as cv
import numpy


kamera = cv.VideoCapture(0)


if not kamera:
    print("Kamera Tidak ada")
    exit('Program Berakhir')

while True:
    
    ret, frame = kamera.read()
    kamera.set(cv.CAP_PROP_FPS,30)
    

    if ret == False:
        print('KEsalahan System') 
    
    try :
        addcolor = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                
        filefaceDetect = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_alt.xml") 
        faceDetector =  filefaceDetect.detectMultiScale(addcolor, scaleFactor=1.1, minNeighbors=1, minSize=((20,20)))
        
     
        for (x, y, w, h) in faceDetector:
            cv.rectangle(addcolor, (x, y), (x + w, y + h), (255, 255, 0), 2)
            
    except:
        print('Tidak file seperti itu')
    
    cv.imshow("camera",addcolor)
    
    if cv.waitKey(1) == ord('x'):
        cv.destroyAllWindows()
        break
    