from firebase import firebase
import RPi.GPIO as GPIO
import frwd as m
##import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
firebase = firebase.FirebaseApplication('https://welcomebiryani-51293.firebaseio.com/', None)

while(1):
    try:
        result = firebase.get('/man', None)
##        print(result)
        try:
            if("None" not in result):
    ##            print("1")
                f=open("buf.txt",'w')
                f.write(str(result))
                if("front" in result):
    ##                m.setup()
                    print("forward")
                    m.forward()
    ##                m.cleanup()
                elif("back" in result):
    ##                m.setup()
                    print("backward")
                    m.backward()
                    
    ##                m.cleanup()
                elif("left" in result):
    ##                m.setup()
                    print("left")
                    m.right()
    ##                m.cleanup()
                elif("right" in result):
    ##                m.setup()
                    print("right")
                    m.left()
    ##                m.cleanup()
                elif("stop" in result):
                    print("stopped")
                    m.stop()
                f.close()
                firebase.delete('/man', None)
            else:
                print("not working")
        except:
            pass
    except KeyboardInterrupt:
        print("none")
        GPIO.cleanup()
