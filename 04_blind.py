import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

servo = 12 #보드 12번 GPIO18
GPIO.setup(servo, GPIO.OUT)
lux = 24 #조도센서 보드24 GPIO8
GPIO.setup(lux, GPIO.IN)
flag = 1 #블라인드 상태 저장 변수. 내려가 있는 것이 1

freq = 100.0
deg_min = 0.0
deg_max = 180.0
dc_min = 5.0
dc_max = 22.0
#모터 그라운드 9번 사용.
def convert_dc(deg):
    return((deg-deg_min)*(dc_max-dc_min)/(deg_max-deg_min)+dc_min)

p = GPIO.PWM(servo, freq)
p.start(0)

while 1:
    if(GPIO.input(lux)==0): #빛이 밝아지고
        if(flag==1):#블라인드가 내려가 있음.
            for deg in range(0,61, 60):
                dc=convert_dc(float(deg))
                p.ChangeDutyCycle(dc)
                flag = 0 #블라인드 올라가 있음.
                time.sleep(1)
    else :#날이 어두우면
        if(flag == 0):#블라인드가 올라가 있으면
            for deg in range(60,-1, -60):
                dc=convert_dc(float(deg))
                p.ChangeDutyCycle(dc)
                flag=1
                time.sleep(1)
GPIO.cleanup()
p.stop()
#GPIO.cleanup()
