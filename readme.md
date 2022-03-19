# Flask APP
***
## Lancement de l'application

Ouvrir le fichier myproject/venv avec VSCode.
Faire Ctrl + Shift + P et choisir l'option "Python: Select Interpreter" et choisir l'option recommandé.
Ouvrir ensuite un terminal et lancer la commande "flask run". Un lien apparaittra avec l'url du site.

## Fonctionnement de l'application

Possibilité d'entrer un ou plusieurs commentaire grâce à un bouton d'ajout d'une zone de texte.
Un second bouton permet ensuite de lancer l'analyse des commentaires et redirige vers une page présentant un tableau qui contient les commentaires saisies, le résultat du modèle (positif ou négatif) ainsi qu'une zone permettant de corriger ou non le résultat obtenu du modèle. Dans le cas d'une correction, le commentaire ainsi que son réel résultat sera alors ajouté au dataset du modèle afin de pouvoir revoir l'apprentissage avec plus de données.