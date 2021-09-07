import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setmode(GPIO.BOARD)

SW = 7
BZ = 16
LED = 18

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BZ, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

root = tk.Tk()
def check_SW(channel):
    key_in = GPIO.input(SW)
    if key_in == 0:
        GPIO.output(LED, GPIO.HIGH)
        GPIO.output(BZ, GPIO.HIGH)
    else:
        GPIO.output(LED, GPIO.LOW)
        GPIO.output(BZ, GPIO.LOW)
GPIO.add_event_detect(SW, GPIO.BOTH, callback=check_SW)
root.mainloop()
GPIO.cleanup()

