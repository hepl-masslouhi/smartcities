# Projet SmartCities

## Description

Dans le cadre du cours « Smartcities & IoT », nous réalisons des projets mettant en œuvre un Raspberry Pi Pico W programmé en MicroPython. Ce cours a pour objectif de nous initier à ce langage à travers l’utilisation d’un [**kit Grove**](https://befr.rs-online.com/web/p/arduino-compatible-boards-kits/1743221) de base.


## Répertoires

- [GPIO](./GPIO/)
- [AD-PWM](./AD-PWM/)
- [LCD](./LCD/)
- [LED_neo](./LED_neo/)
- [network](./network/)
- [sensors](./sensors/)


## Raspberry Pi Pico W

Le Raspberry Pi Pico W est une version améliorée du Pico, intégrant une connectivité Wi-Fi et Bluetooth.
Ce microcontrôleur se distingue notamment par les caractéristiques suivantes :

- Processeur dual-core Arm Cortex-M0+ cadencé à 133 MHz

- 264 Ko de SRAM et 2 Mo de mémoire Flash intégrée

- Connectivité Wi-Fi 802.11n et Bluetooth 5.2 (BLE)

- 26 broches GPIO multifonctions, compatibles avec de nombreux capteurs et modules Grove

- ADC 12 bit 500ksps


<img width="842" height="595" alt="Image" src="https://github.com/user-attachments/assets/ab5ba168-6314-4fbd-9100-8d96290e6bcc" />


# MicroPython

<img width="100" height="100" alt="Image" src="https://github.com/user-attachments/assets/e25d1f89-a009-4b33-8769-b4b13fe0f5e8" />



MicroPython est une adaptation du langage Python conçue pour fonctionner sur des microcontrôleurs.
Sa structure s’organise autour de plusieurs éléments essentiels :

- Un portage complet du langage Python : les mots-clés, objets et fonctions intégrées (built-in) sont disponibles dans une version allégée, adaptée aux ressources limitées des microcontrôleurs.
- Des modules standards allégés : une vingtaine de modules Python classiques ont été adaptés pour MicroPython, tout en conservant leurs fonctions principales. Parmi eux figurent notamment re (expressions régulières), time, sys, os, io et math.
- Des modules spécifiques à MicroPython : ces modules regroupent les classes et fonctions communes nécessaires à l’exploitation du matériel des microcontrôleurs.
- Des modules dédiés à chaque plateforme : ils fournissent les classes et fonctions propres à une carte donnée, permettant une intégration optimale.
- Des modules “librairies” matériels : ils offrent les outils indispensables à la gestion des composants physiques tels que capteurs, modules ou cartes d’extension.


# Visual Studio Code

<img width="100" height="100" alt="Image" src="https://github.com/user-attachments/assets/c8c247fe-ab5e-43ec-9325-5a7f1a45c9ba" />



J’ai choisi comme environnement de développement Visual Studio Code, un IDE qui permet de programmer dans quasiment tous les langages existants.

Pour programmer en MicroPython sur le Raspberry Pi Pico W, il suffit d’ajouter l’extension MicroPico.

