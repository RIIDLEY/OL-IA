import pathlib
from flask import Flask, jsonify, redirect, render_template, session, request, url_for
import subprocess as sp
import pickle

from numpy import array
app = Flask(__name__)
filenameModel = '\model\\finalized_model.sav'
filenameVectorizer = '\model\\vectorizer.sav'
modelPath = str(pathlib.Path(__file__).parent)


# https://pythonise.com/series/learning-flask/flask-working-with-forms

@app.route('/')
def index():
   return redirect(url_for("comment_page"))

@app.route('/comment_page', methods=["GET", "POST"])
def comment_page():
    if request.method == "POST":
        requestData = request.form
        session["requestData"] = requestData
        return redirect(url_for("comment_page_result", requestData=requestData))

    return render_template("comment_page.html")


@app.route('/comment_page_result', methods=["GET", "POST"])
def comment_page_result():
    if request.method == "POST":
        requestData = request.form

        loaded_model = pickle.load(open(modelPath + filenameModel, 'rb'))
        vectorizer = pickle.load(open(modelPath + filenameVectorizer, 'rb'))
        commentResult = dict()
        for i in requestData:
            commentaire = [requestData.get(i)]
            commentaire = vectorizer.transform(commentaire)
            commentResult[requestData.get(
                i)] = loaded_model.predict(commentaire)[0]

        print(commentResult)
    return render_template("comment_page_result.html", commentResult=commentResult)
