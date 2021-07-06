import cv2

facecascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
framewidth=640
frameheight=480
cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)
cap.set(10,130)
while True:
    success,img=cap.read()
    imgb=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=facecascade.detectMultiScale(imgb,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("result",img)
    if cv2.waitKey(1) &0xFF ==ord('q'):
        break



#
#img=cv2.imread("friend.jpg")
#imggr=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
#faces=facecascade.detectMultiScale(imggr,1.1,4)
#
#for (x,y,w,h) in faces:
#    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#
#
#cv2.imshow("Result",img)
##cv2.imshow("Re",imggr)
#cv2.waitKey(0)