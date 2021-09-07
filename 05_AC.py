import time
import Adafruit_DHT
import RPi.GPIO as GPIO
import RPi_I2C_driver
mylcd = RPi_I2C_driver.lcd()
sensor = Adafruit_DHT.DHT   11
pin = 17
LED = 27 #13
def sendSignal() :
    for k in range(4):
        GPIO.output(pins[k], signal[step][k])
GPIO.setwarnings(False)        
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
pins = [12,16,20,21] #IN1, IN2, IN3, IN4
for p in pins:
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, GPIO.LOW)

FULL_STEP = 4
HALF_STEP = 8

signal_full = [
          [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW],
          [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
          [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW],
          [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH]
          ]

signal_half = [
          [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH],
          [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW],
          [GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
          [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
          [GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW],
          [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW],
          [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH],
          [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH],
          ]

#stepping mode and direction
steps = FULL_STEP
signal = signal_full
clockwise = True
try:
    while True:
        h , t = Adafruit_DHT.read_retry(sensor, pin)
        if h is not None and t is not None:
            #lcd와 콘솔에 온도, 습도 표시
            print("Temperature = {0:0.1f}*C\nHumidity = {1:0.1f}%".format(t,h))
            mylcd.lcd_display_string("T:{0:0.1f}*C H:{1:0.1f}%".format(t, h),1)
            #불쾌지수 계산
            thi = (t+h)*0.72+40.6
            if( thi > 90 ):
                GPIO.output(LED, GPIO.HIGH)
                for i in range(512):
                    if clockwise :
                        for step in range(steps):
                            sendSignal()
                            time.sleep(0.01)
                    else :
                        for step in reversed(range(steps)):
                            sendSignal()
                            time.sleep(0.01)
            else:
                GPIO.output(LED, GPIO.LOW)
                
            print((t+h)*0.72+40.6)
            
            
        else:
            print("Read error")
        time.sleep(1)
except KeyboardInterrupt:
    print("f")
          
finally:
          print("End of Program")

