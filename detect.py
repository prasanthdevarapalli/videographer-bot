import cv2
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)

##cascPath = sys.argv[1]
pwm=GPIO.PWM(37,50)
faceCascade = cv2.CascadeClassifier("/home/pi/Downloads/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)
i=6
pwm.start(i)

try:
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(20, 20),
    ##        flags=cv2.CV_HAAR_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    ##        roi_gray= gray[y:y+h, x:x+w]
            getx=int(x)
            print("x=  "+str(getx))
            gety=int(y)
            print("y=  "+str(gety))
    ##        time.sleep(0.5)
            if(getx<150 and i<12.5):
                i=i+0.3
                pwm.ChangeDutyCycle(i)
                time.sleep(0.1)
    ##servo
            elif(getx>400 and i>0):
                i=i-0.3
                pwm.ChangeDutyCycle(i)
                time.sleep(0.1)
            else:
                print("servo maximum angle")
    ##servo            
                

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
except KeyboardInterrupt:
    pass
GPIO.cleanup()
