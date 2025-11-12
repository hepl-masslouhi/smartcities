# Contrôle d'une horloge avec Raspberry Pi Pico W et servo moteur

## Objectif

Ce projet permet de réaliser une horloge connectée avec un Raspberry Pi Pico W et un servo moteur.  
L’heure est récupérée automatiquement via Internet et la position du servo varie pour indiquer l’heure actuelle.  
Un bouton permet de changer le fuseau horaire et d’activer le mode 24 heures.

## Matériel

- Raspberry Pi Pico W  
- Servo moteur  
- Bouton poussoir  
- Fils de connexion  

## Fonctionnalités

#### Connexion à Internet
- Le Pico W se connecte au réseau Wi-Fi via la bibliothèque `network`.  
- L’heure est récupérée automatiquement depuis le serveur NTP.

#### Calcul de l’angle du servo
- Le servo peut tourner entre 0° et 180°.  
- L’angle correspond à la position de l’aiguille sur le cadran d’horloge :  
  - 12h → 0°  
  - 6h → 90°  
- Chaque heure correspond à 15° (180° ÷ 12 heures).

#### Contrôle du servo
- L’angle est calculé en fonction de l’heure actuelle.  
- Le servo se déplace automatiquement pour indiquer la bonne heure.  
- Le contrôle se fait via la bibliothèque `machine` (PWM sur une broche du Pico).

#### Changement de fuseau horaire
- Un appui simple sur le bouton permet de changer le fuseau horaire (ex. UTC, UTC+1, UTC-5, etc.).  
- L’heure affichée s’ajuste automatiquement selon le décalage sélectionné.

#### Mode 24 heures
- Un double clic rapide sur le bouton active le mode 24h.  
- Dans ce mode :  
  - 0h → 0°  
  - 12h → 90°  
- Le servo couvre toute la journée sur 180°.

## Utilisation

1. Connecter le Raspberry Pi Pico W à l’ordinateur.  
2. Copier le script MicroPython sur le Pico.  
3. Mettre à jour vos identifiants Wi-Fi dans le code.  
4. Exécuter le programme.  
5. Observer le servo indiquer l’heure actuelle et répondre aux appuis sur le bouton.

## Diagramme du code

