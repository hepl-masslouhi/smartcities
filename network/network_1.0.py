import network
import ntptime
import time
from machine import Pin, PWM

# Configuration 
SSID = 'iPhone'
PASSWORD = '123456789..'
servo = PWM(Pin(18), freq=50)
button = Pin(20, Pin.IN)

# Initialisation du wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)


click_count = 0                                                 # Compteur de clics
last_press_time = 0                                             # Temps du dernier clic sur le bouton
last_action_time = 0                                            # Temps de la derniere action
double_click_mode = False                                       # Mode 12h ou 24h
timezone_index = 0                                              # Fuseau recupere 
TIMEZONES = [0, 1, 2, -5, 9]                                    # Liste des decalages horaires

# Interruption 
def button_irq(pin):                                                          # Detecter un clic plus facilment grace a l'interruption
    global click_count, last_press_time
    now = time.ticks_ms()
    if time.ticks_diff(now, last_press_time) < 200:                           # Anti-rebond pour le bouton mecanique
        return
    click_count += 1
    last_press_time = now

button.irq(trigger=Pin.IRQ_FALLING, handler=button_irq)

# Calcul positio du servo
def set_angle(angle):
    duty = int((angle / 180 * 2000) + 500) 
    servo.duty_u16(int(duty / 20000 * 65535))

# Calcul de l'angle (12H)
def hour_to_angle(hour):
    return (hour % 12) * 15                     # 12h = 180° ==> 15° par heure

# Calcul de l'angle (24H)
def hour_to_angle_24h(hour):
    return (hour / 24) * 180                    # 24h = 180° ==> 7,5° par heure

# Attente pour la connexion wifi
while not wlan.isconnected():
    time.sleep(1)

# Synchronisation de l'heure via NTP 
try:
    ntptime.settime()
except Exception as e:
    print("Erreur NTP :", e)


while True:
    now = time.ticks_ms()

    # --- Gestion des clics ---
    if click_count > 0 and time.ticks_diff(now, last_press_time) > 400:
        if click_count == 1:                                                                # Quand un clic est detcte un changement de fuseau est effectue
            timezone_index = (timezone_index + 1) % len(TIMEZONES)
            print("Fuseau horaire : UTC%+d" % TIMEZONES[timezone_index])
        elif click_count >= 2:
            double_click_mode = not double_click_mode                                       # Double clic ==> changer de mode 12h / 24h
            print("Mode 24h =", double_click_mode)
        click_count = 0

    # Calcul du fuseau horaire
    offset = TIMEZONES[timezone_index] * 3600   # 1h = 3600s
    t = time.localtime(time.time() + offset)

    # afficher l'heure 
    if double_click_mode:
        # Format 24h
        heure = "%02d:%02d:%02d" % (t[3], t[4], t[5])
        angle = hour_to_angle_24h(t[3])
    else:
        # Format 12h avec AM/PM
        hour_12 = t[3] % 12 or 12
        suffix = "AM" if t[3] < 12 else "PM"
        heure = "%02d:%02d:%02d %s" % (hour_12, t[4], t[5], suffix)
        angle = hour_to_angle(t[3])

    # Maj chaque 2s
    if time.ticks_diff(now, last_action_time) > 2000:
        print(heure, "Angle:", angle)
        set_angle(angle)
        last_action_time = now

