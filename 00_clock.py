import sys
import time
import datetime
import RPi.GPIO as GPIO
import tm1637
#그라운드 14번핀 사용
houseClock = tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL) #출력핀 각각 GPIO23 24-> 16번 18번

houseClock.Clear()
houseClock.SetBrightnes(10)

while(True):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    currenttime = [int(hour/10), hour%10, int(minute/10), minute%10]
    
    houseClock.Show(currenttime)
    houseClock.ShowDoublepoint(second%2)
    
    time.sleep(1)