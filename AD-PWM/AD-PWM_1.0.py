from machine import Pin, PWM, ADC
from time import sleep

buzzer = PWM(Pin(27))
LED = PWM(Pin(18))
BUTTON = Pin(16, Pin.IN, Pin.PULL_DOWN)

# ADC 0 sur pin 26 
volume_adc = ADC(0)

val = 0

# Interruption avec le bouton
def button_handler(pin):
    global val
    val = 1 - val                                                   # Quand val = 0 ==> melodie_1, val = 1 ==> melodie_2

BUTTON.irq(trigger=Pin.IRQ_RISING, handler=button_handler)


# Fonction de lecture de mélodie
def joue_melodie(melodie):
    global val
    for note in melodie:                              
                                                                    # Si le bouton est pressé, on change de mélodie
        if val == 1 and melodie == melodie_1:                       # Si on joue melodie_1 et val devient 1 ==> arrêt pour jouer l'autre mélodie
            return
        elif val == 0 and melodie == melodie_2:                     # Si on joue melodie_2 et val devient 0 ==> arrêt pour jouer l'autre mélodie
            return
        
        vol = int((volume_adc.read_u16() / 65535) * 4000)           # Lecture du volume

        # Jouer la note
        buzzer.freq(notes[note])
        LED.freq(notes[note])
        buzzer.duty_u16(vol)
        LED.duty_u16(65535)                                         # LED allumée au maximum
        sleep(0.2)

        # Pause entre les notes
        buzzer.duty_u16(0)
        LED.duty_u16(0)
        sleep(0.05)


# Notes avec les fréquences 
notes = {
    'G': 392,
    'C': 261,
    'D#': 622,
    'F': 349,
    'A#': 466,
    'D': 294,
    'A': 440,
    'G#': 415,
    'C2': 523,
    'E': 329  
}

melodie_1 = [
    'G', 'C', 'D#', 'F', 'G', 'C', 'D#', 'F',
    'G', 'C', 'D#', 'F', 'G', 'C', 'E', 'F',
    'G', 'C', 'E', 'F', 'G', 'C', 'E', 'F',
    'G', 'C', 'E', 'F', 'G', 'C', 'D#', 'F',
    'G', 'C', 'D#', 'F', 'D', 'F', 'A#', 'D#',
    'D', 'F', 'A#', 'D#', 'D', 'C', 'G', 'C',
    'D#', 'F', 'G', 'C', 'D#', 'F', 'D', 'F',
    'A#', 'D#', 'D', 'F', 'A#', 'D#', 'D', 'C'
]

melodie_2 = [
    'E', 'E', 'E', 'C', 'E', 'G', 'G',
    'C', 'G', 'E', 'A', 'D', 'A', 'A',
    'G', 'E', 'G', 'A', 'F', 'G', 'E',
    'C', 'D', 'D', 'C2', 'C2'
]



while True:
    if val == 0:
        joue_melodie(melodie_1)
    else:
        joue_melodie(melodie_2)