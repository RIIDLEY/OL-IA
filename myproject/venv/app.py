from ctypes import sizeof
import pathlib
from flask import Flask, jsonify, redirect, render_template, session, request, url_for
import subprocess as sp
import pickle
import os
import subprocess

from numpy import array
app = Flask(__name__)
modelPath = str(pathlib.Path(__file__).parent)

#fichier du modele apres apprentissage
filenameModel = '\model\\model.sav'
#fichier du vectorizer apres initialisation
filenameVectorizer = '\model\\vectorizer.sav'
#dataset temporaire
temp_dataset = "dataset_temp.txt"
#dataset final
dataset = "dataset.txt"


# https://pythonise.com/series/learning-flask/flask-working-with-forms

@app.route('/')
def index():
   return redirect(url_for("comment_page"))

@app.route('/comment_page', methods=["GET", "POST"])
def comment_page():
    dataPost = False
    if request.method == "POST":
        dataPost = True
        requestData = request.form

        #variables des inputs de correction
        commentVal = "comment_"
        resultModelVal = "resultModel_"
        correctionVal = "correction_"

        #ouverture (create if not exist) du dataset temporaire
        fileTemp = open(temp_dataset, "a+")

        #permet d'obtenir le nombre de commentaires saisies et leurs valeurs en fonction du nombre d'input 
        # (si 6 inputs venant du POST, il y a donc 2 commentaires saisies)  
        valTemp = int(len(requestData)/3)

        for i in range(valTemp):
            #valeur de l'input "comment_i"
            commentVal1 = commentVal + str(i)
            comment = requestData.get(commentVal1)

            #valeur de l'input "resultModel_i"
            resultModelVal1 = resultModelVal + str(i)
            resultModel = requestData.get(resultModelVal1)

            #valeur de l'input "correction_i
            correctionVal1 = correctionVal + str(i)
            correction = requestData.get(correctionVal1)

            #les variables (comment, resulModel, correction) correcspondent au
                #commentaire saisie
                #resultat provenant du model
                #si le resultat du modele est correcte ou non (corrigé par l'utilisateur)
                

            #si le resultat du modele est mauvais
            #remplace la valeur du resultat du model par son inverse (positive <=> negative)
            if correction == "false":
                if resultModel == "positive":
                    resultModel = "negative"
                else:
                    resultModel = "positive"

                #ecriture des donnes a corriger dans un dataset temporaire
                #sous la forme name;comment;sentiment
                fileTemp.write("reviewTitle;" + comment + ";" + resultModel + "\n")
        fileTemp.close()

        #concatenation du fichier dataset temporaire au dataset final s'il y a plus de 100 lignes dans le dataset temporaire
        mergeDataDataset(dataset, temp_dataset)
            

    return render_template("comment_page.html", dataPost=dataPost)

#methode pour avoir le nombre de ligne d'un fichier passé en paramètre
def getCountOfLines(file):
    fp = open(file, "r")
    linesCount = len(fp.readlines())
    return linesCount

#methode pour ajouter les lignes du dataset temporaire au dataset final
def mergeDataDataset(dataset, temp_dataset):
    #si le fichier dataset temporaire contient plus de 100 lignes
    if getCountOfLines(temp_dataset) > 100:
        #ouverture du dataset temporaire en lecture (read) et du dataset final en ecriture (append)
        with open(temp_dataset,'r') as datasetT, open(dataset,'a') as datasetF:
            #pour chaque ligne du fichier dataset temporaire
            for line in datasetT:
                #ajoute les lignes du dataset temporaire au dataset final
                datasetF.write(line)
        print("concatenation du dataset temporaire au dataset final réussi!")

        #vide le contenu du dataset temporaire
        f = open(temp_dataset,"w")
        f.close()
        print("dataset temporaire vide!")
        
        print("Relance du script du modele...")
        subprocess.Popen(["python", "project.py"])
        #os.system("project.py")
        #print("Script du modele executé avec succès!")




@app.route('/comment_page_result', methods=["GET", "POST"])
def comment_page_result():
    if request.method == "POST":
        requestData = request.form

        #chargement du modele et du vectorizer sauvegardé
        loaded_model = pickle.load(open(modelPath + filenameModel, 'rb'))
        vectorizer = pickle.load(open(modelPath + filenameVectorizer, 'rb'))
        #creation d'un dictionnaire qui contiendra l'ensemble des commentaires saisies avec leurs prediction provenant du modele
        commentResult = dict()
        indexI = 0
        for i in requestData:
            #recuperation du commentaire via le POST
            commentaire = [requestData.get(i)]
            #transformation du commentaire via le vectorizer afin de pouvoir etre comprehensible par le modele 
            commentaire = vectorizer.transform(commentaire)
            #ajout des informations dans le dictionnaire commentResult sous la forme {comment:'commentaireSaisie', comment_result:'predictionDuModele'}
            commentResult[indexI] = {'comment':requestData.get(i), 'comment_result':loaded_model.predict(commentaire)[0]}

            indexI += 1
        
        return render_template("comment_page_result.html", commentResult=commentResult)
