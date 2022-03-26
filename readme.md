# Flask APP
***
## Pré-requis

Installation du framework Flask: https://flask.palletsprojects.com/en/2.0.x/installation/
Python installé: https://www.python.org/downloads/

## Lancement de l'application

Ouvrir un terminal et se placer dans le répertoire myproject/venv.
Lancer ensuite la commande "flask run". Un lien apparaittra avec l'url du site.

## Fonctionnement de l'application

Possibilité d'entrer un ou plusieurs commentaire grâce à un bouton d'ajout d'une zone de texte.
Un second bouton permet ensuite de lancer l'analyse des commentaires et redirige vers une page présentant un tableau qui contient les commentaires saisies, le résultat du modèle (positif ou négatif) ainsi qu'une zone permettant de corriger ou non le résultat obtenu du modèle.
Dans le cas d'une correction, le commentaire ainsi que son réel résultat sera alors ajouté au dataset du modèle afin de pouvoir revoir l'apprentissage avec plus de données. Cet ajout ne se réalise que lorsqu'il y a un certain nombre de lignes dans le fichier temporaire.
