# Contrôle d'une LED RGB au rythme de la musique

## Objectif

Ce projet permet de synchroniser une LED RGB avec la musique.  
La LED change de couleur automatiquement au rythme détecté par un microphone connecté au Raspberry Pi Pico W.  
Le rythme est également calculé en BPM et les valeurs moyennes sont sauvegardées dans un fichier texte sur le Pico.

## Matériel

- Raspberry Pi Pico W  
- Module microphone 
- Module LED RGB (WS2812) 
- Fils de connexion  

## Fonctionnalités

- Lecture continue des données sonores via le microphone.  
- Détection des battements de la musique.  
- Changement aléatoire de couleur de la LED à chaque battement, visible et synchronisé.  
- Calcul du rythme en BPM et moyenne toutes les minutes.  
- Enregistrement des BPM moyens dans le fichier BPM.txt sur le Pico.  

## Utilisation

1. Connecter le microphone sur l’ADC et la LED RGB sur un GPIO du Pico.  
2. Copier le script MicroPython sur le Pico.  
3. Exécuter le script.  
4. Observer la LED changer de couleur au rythme de la musique.  
5. Vérifier le fichier BPM.txt pour les valeurs moyennes de BPM.  

## Paramètres à ajuster

- `seuil` : niveau sonore pour détecter un battement (à ajuster selon le bruit ambiant).  
- `t_min` : intervalle minimal entre deux battements (ms) pour éviter les fausses détections.  

## Diagramme du code

<img width="441" height="644" alt="Image" src="https://github.com/user-attachments/assets/cb2fa0f7-4086-4456-8528-d5cc0b915c3d" />



