#  Hand Tracking & Finger Counting with OpenCV & MediaPipe

Ce projet utilise **OpenCV** et **MediaPipe** pour détecter une main via la webcam et compter le nombre de doigts levés en temps réel. Le résultat est affiché directement à l'écran avec les points de repère (landmarks) de la main dessinés.

## Fonctionnalités

- Suivi en temps réel d'une seule main via webcam
- Détection et affichage des doigts levés
- Visualisation des points et connexions de la main
- Affichage dynamique du nombre de doigts détectés

## Technologies

- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)

## Installation

1. Clone le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/nom-du-projet.git
   cd nom-du-projet  

2. Installer les dépendances
   ```bash
   pip install opencv-python mediapipe

 ## Exécution
 ```bash
python hand_finger_detection.py
Appuie sur q pour fermer la fenêtre de la webcam.
