#   Program Sederana Pendeteksi Wajah Pada manusia
menggunakan opencv dan Imtuils


pada bagian ini jika ingin menggunakan Gambar berwarna silakan hapusvariabel add color
 HAPUS--> addcolor = cv.cvtColor(frame, cv.COLOR_BGR2GRAY
 
 lalu pada ini addcolor diganti dengan variabel frame
 <br>|
 <br>|----------------------|----------------------------|<br>
                                                     |
 faceDetector =  filefaceDetect.detectMultiScale(addcolor, scaleFactor=1.1, minNeighbors=1, minSize=((20,20)))


lalu pada diganti juga dengan frame 
-----> imshow(frame)
