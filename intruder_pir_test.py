import RPi.GPIO as GPIO
import time
from picamera import PiCamera
GPIO.setmode(GPIO.BOARD) #Set GPIO to pin numbering
pir = 8 #Assign pin 8 to PIR
led = 10 #Assign pin 10 to LED
GPIO.setup(pir, GPIO.IN) #Setup GPIO pin PIR as input
GPIO.setup(led, GPIO.OUT) #Setup GPIO pin for LED as output
print ("Sensor initializing . . .")
time.sleep(2) #Give sensor time to startup 
print ("Active")
print ("Press Ctrl+c to end program")
camera = PiCamera()
camera.resolution = (640, 480)
#camera.resolution = (1024, 768)

try:    
    while True:
        
        if GPIO.input(pir) == True: #If PIR pin goes high, motion is detected
            print ("Motion Detected!")
            GPIO.output(led, True)#Turn on LED
            camera.start_preview()
            camera.annotate_text = 'Intruder !!'
            time.sleep(2)
            #camera.capture('foo.jpg')
            camera.capture('foo1.jpg', resize=(320, 240))
            camera.stop_preview()
            time.sleep(4) #Keep LED on for 4 seconds
            GPIO.output(led, False) #Turn off LED
            time.sleep(2)
except KeyboardInterrupt: #Ctrl+c 
    pass #Do nothing, continue to finally
finally:
    GPIO.output(led, False) #Turn off LED in case left on
    GPIO.cleanup() #reset all GPIO
    print ("Program ended")
