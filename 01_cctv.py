import RPi.GPIO as GPIO
import picamera
import time
import datetime

#5V전원, 14번 혹은20번 그라운드 사용.
GPIO.setmode(GPIO.BOARD)
savepath = '/home/pi/Desktop'
port=29 #GPIO 5번 in BOARD 29번  , lcd를 위해 수정 필요  
GPIO.setup(port,GPIO.IN)

while 1:
    time.sleep(1)
    print(GPIO.input(port))
    if(GPIO.input(port)==0):
        with picamera.PiCamera() as camera:
            #camera = picamera.picamera()
            #camera.resolution = (1024,768)
            now = datetime.datetime.now()
            filename = now.strftime('%Y-%m-%d %H:%M:%S')
            camera.start_recording(output = savepath +'/' + filename + '.h264')
            camera.wait_recording(3)
            camera.stop_recording()          
GPIO.cleanup()



