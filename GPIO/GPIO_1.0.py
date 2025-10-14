from machine import Pin
from time import sleep

LED = Pin(18, Pin.OUT)
BUTTON = Pin(16, Pin.IN, Pin.PULL_DOWN)

val = 0

def button_handler (pin):
    global val
    sleep(0.01)
    if  val >= 3:
        val = 0
    else:
        val += 1

BUTTON.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

while True:
    if val == 1:
        LED.toggle()
        sleep(2)
    elif val == 2: 
        LED.toggle()
        sleep(1)
    else:
        LED.value(0)
