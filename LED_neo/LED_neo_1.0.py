from machine import Pin, ADC
from utime import sleep_ms, ticks_ms, ticks_diff
from ws2812 import WS2812
import urandom

# Initialisation
micro = ADC(2)              # Micro
led = WS2812(20, 1)         # Led RGB

# Parametres
average = 60000             # 1m en ms pour le calcul de la moyenne
seuil = 60                  # Seuil pour le declenchement à adapter en fonction du bruit autour
t_min = 200                 # Temps minimal entre deux pics (300 BPM MAX)
                 

t_beat = ticks_ms()            # Dernier battement 
t_average = ticks_ms()         # Pour commencer la periode de la moyenne 
liste_bpm = []                 # Liste des BPM pour faire la moyenne


# Fonction pour les couleurs aleatoires
def random_color(): 
    r = urandom.getrandbits(8) 
    g = urandom.getrandbits(8) 
    b = urandom.getrandbits(8) 
    return (r, g, b)

while True:

    t_now = ticks_ms()
    mic_val = micro.read_u16() / 256                                # Lecture du micro de 0 à 255


    if mic_val > seuil and ticks_diff(t_now, t_beat) > t_min:       # Si signal > seuil et que t_min est ecoulee ==> nouveau battement
        dt = ticks_diff(t_now, t_beat)
        t_beat = t_now

        bpm = 60000 / dt
        liste_bpm.append(bpm)

        led.pixels_fill(random_color())                             # Clignotement LED
        led.pixels_show()


    if ticks_diff(t_now, t_average) >= average and liste_bpm:       # Calcule et affiche la moyenne quand 1m est ecoulee
        bpm_moy = int(sum(liste_bpm) / len(liste_bpm))
        print("Moyenne:", bpm_moy, "BPM")

        with open("BPM.txt", "a") as f:                             # Ecriture dans le fichier BPM
            f.write(str(bpm_moy) + "\n")

        t_average = t_now
        liste_bpm.clear()

    sleep_ms(10)                                                    # Pour eviter d'avoir des lectures trop rapides