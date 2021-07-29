from time import sleep
from picamera import PiCamera

camera=PiCamera()
camera.resolution=(1024,768)
camera.start_preview()
sleep(2)
camera.capture('picture1.jpg')
camera.stop_preview()
camera.annotate_text='hello world!'
camera.start_preview()
sleep(2)
camera.capture('picture2.jpg')
camera.stop_preview()
camera.start_preview()
sleep(2)
camera.capture('picture3.jpg',resize=(320,240))
camera.stop_preview()
camera.resolution=(640,480)
camera.start_recording('my video.h264')
camera.wait_recording(30)
camera.stop_recording()

