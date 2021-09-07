import time
import smbus
import LCD1602
#import wiringpi as wire
import RPi.GPIO as GPIO

IRval=7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IRval,GPIO.IN)
#LCD1602.init(0x27, 1)

while 1:
    LCD1602.init(0x27, 1)
    LCD1602.write(4, 0, 'watching')
    LCD1602.write(7, 1, 'TV!')
    time.sleep(1)
    if (GPIO.input(IRval)==0):
        #LCD1602.write(0, 0, 'watching TV~~')
        LCD1602.clear()
        time.sleep(5)
    
GPIO.cleanup()