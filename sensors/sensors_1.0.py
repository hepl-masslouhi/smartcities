from machine import Pin, I2C, ADC, PWM
from time import sleep
from lcd1602 import LCD1602
import dht

# Initialisation du matériel
pot = ADC(0)
led = Pin(18, Pin.OUT)
buzzer = PWM(Pin(1))
buzzer.duty_u16(0)
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
lcd = LCD1602(i2c, 2, 16)
lcd.clear()
sensor = dht.DHT11(Pin(20))

# Fréquence du buzzer
buzzer_fr = 1000
 
# Convertit la valeur du potentiometre en temp (15 à 33°)
def map_temp(adc_value):
    return 15 + (adc_value / 65535) * (35 - 15)
 
while True:
        # Lecture de la température
        sensor.measure()
        temp = sensor.temperature()
 
        # Lecture potentiomètre
        pot_val = pot.read_u16()
        temp_set = int(map_temp(pot_val))
 
        # Affichage sur l'ecran
        lcd.setCursor(0, 0)
        lcd.print(f"Set:{temp_set:2d}C    ")
        lcd.setCursor(0, 1)
        lcd.print(f"Ambient:{temp:2d}C  ")
 
        # Gestion LED et buzzer
        if temp > temp_set + 3:
            # Trop chaud ==> clignote vite et buzzer ON
            led.value(1)
            buzzer.freq(buzzer_fr)
            buzzer.duty_u16(32768)
            lcd.setCursor(10, 1)
            lcd.print("ALARM")  
            sleep(0.5)
            led.value(0)
            buzzer.duty_u16(0) 
            sleep(0.5)
        elif temp > temp_set:
            # Un peu chaud ==> clignote lentement, pas de son
            led.value(1)
            buzzer.duty_u16(0)
            lcd.setCursor(10, 1)
            lcd.print("     ") 
            sleep(1)
            led.value(0)
            sleep(1)
        else:
            # Température correcte ==> tout éteint
            led.value(0)
            buzzer.duty_u16(0)
            lcd.setCursor(10, 1)
            lcd.print("     ") 
            sleep(1)
 