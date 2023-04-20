# Titre de notre projet

Mon musée

## Description

Ce projet est composé d’ une application web contenant des fonctionnalités d'un site web dynamique  qui est composée de 2 compartiments (Utilisateur et administrateur )et  une application mobile Android  dans le but d’informer les touristes et même les locuteurs natifs des musées existants en Tunisie. 


## Installation

#pour le site web :

Django==3.2.7
django-cors-headers==3.8.0
djangorestframework==3.12.4

#pour l'application mobile :

react-native==0.70.5
node.js==18.12.1



--> Déplacez-vous dans le répertoire où se trouvent les fichiers du projet (site web):

```bash
cd my_museum

````

--> Créer un environnement virtuel :

```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

````

--> Activez votre environnement virtuel :

```bash
envname\scripts\activate

```

--> Installer les exigences :

```bash
pip install -r requirement_name

## Usage

--> Pour exécuter l application web, nous utilisons :

```bash
python manage.py runserver

```

> ⚠  Ensuite, le serveur de développement sera démarré à l'adresse http://127.0.0.1:8000/.


## Crédits

Liste des contributeurs, y compris leurs rôles et responsabilités:

Amal Maatoug + Ahmed Zahaf : partie web
Imen khalil + Tassnim Chiba : partie mobile

## Références

https://docs.djangoproject.com/en/4.1/

https://reactnative.dev/docs/getting-started
