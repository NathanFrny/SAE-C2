# SAE C2

Auteur : Nathan Fourny et Noah Bonnel  
Date : 19/11/2023

## Contexte

L'observatoire de Springfield est confronté à un défi majeur : la pollution lumineuse urbaine empêche les observations astronomiques claires. Des panneaux lumineux excessifs ont transformé la ville en une mer de lumières, rendant le ciel nocturne presque impossible à étudier.

## Présentation

Ce projet vise à créer une application permettant de traiter les images astronomiques affectées par la pollution lumineuse. L'objectif est de développer une interface en Python utilisant la bibliothèque OpenCV pour éliminer le gradient lumineux des images fournies.

## Features de l'application

Notre application possède les fonctionnalitées suivantes :

* Insérer une image
* Supprimer le voile de pollution lumineuse en soustrayant un gradient donné en paramètre
* Supprimer le voile de pollution lumineuse par l'intermédiaire d'un gradient linéaire
* Modifier des paramètres d'images (Gamma, Saturation, Flou)
* Insérer plusieurs images et naviguer entre elles

## Comment l'utiliser

* **Ajouter une image**  
    -> Cliquez sur le bouton "Charger une image"  
    -> Sélectionnez l'image que vous voulez insérer  
    -> Vous pouvez désormais visualiser votre image  

* **Supprimer le voile de pollution lumineuse en soustrayant un gradient donné en paramètre**  
    -> Ajoutez une image  
    -> Sélectionnez dans la checkbox "soustraction du gradient"  
    -> Insérez le gradient demandé  
    -> Cliquez sur générer l'image  
    -> Vous pouvez visualiser la nouvelle image générée  

* **Supprimer le voile de pollution lumineuse par l'intermédiaire d'un gradient linéaire**  
    -> Ajoutez une image  
    -> Sélectionnez dans la checkbox 'Gradient linéaire"  
    -> Cliquez sur générer l'image  
    -> Vous pouvez visualiser la nouvelle image générée  

* **Modifier une image**   
    -> Ajoutez une image  
    -> Cochez les paramètres que vous voulez modifier (Saturation, Gamma ou Flou)  
    -> Modifiez les valeurs grâce au sliders ou directement dans le champs des valeurs  
    -> Vous pouvez visualiser votre image modifiée  

* **Naviguer entre les images**  
    -> Ajouter 2 images  
    -> Cliquez sur "Suivant" pour aller vers l'image suivante  
    -> Cliquez sur "Précédent" pour aller vers l'image précédente  

    *Remarque : Cliquer sur suivant alors que vous êtes sur la dernière image vous renvois vers la première (et inversement)*

## Comment lancer l'application ?

* **Depuis VScode**
    -> Lancer le projet depuis le répertoire SAE-C2  
    -> Rendez-vous dans App/Controller.py  
    -> Executez le fichier

* **Depuis un terminal**  
    -> Lancer un terminal
    -> Rendez vous dans le dossier SAE-C2 (il contient normalement le dossier App et le dossier Images)  
    -> Executez la commande suivante  

    ```py
    python App/Controlleur.py
    ```

    -> L'application être exécutée  

* **Depuis l'application**  
    -> Rendez-vous dans le dossier SAE-C2/dist/Controlleur/  
    -> Vous y trouver un fichier nommé Controlleur.exe  
    -> Ouvrez ce fichier  
    -> l'application se lance  

## Informations complémentaire

* Lorsque vous voulez soustraire un gradient à une image (gradient en paramètre). Le gradient doit impérativement faire la même taille que l'image.
* Code entièrement écrit en anglais
* Pour une réutilisation référez-vous aux informations mises en début de chaque script
* Changer d'image (suivant et précédent) ne va pas sauvegarder vos modifications