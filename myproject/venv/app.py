from flask import Flask, jsonify, redirect, render_template, session,request, url_for
import subprocess as sp
app = Flask(__name__)

#https://pythonise.com/series/learning-flask/flask-working-with-forms

@app.route('/comment_page', methods=["GET", "POST"])
def comment_page():

   if request.method == "POST":
      requestData = request.form
      #print(requestData)
      session["requestData"] = requestData
      return redirect(url_for("comment_page_result", requestData = requestData))
      #comment_page_result(request)
      #return jsonify(req)
   #comment_page_result()

   return render_template("comment_page.html")



@app.route('/comment_page_result', methods=["GET", "POST"])
def comment_page_result():
   #comment_page()
   if request.method == "POST":
      requestData = request.form
      print(requestData)
      #session["requestData"] = requestData
   #requestData = session.get("requestData")
   #print(session)
   return render_template("comment_page_result.html", requestData=requestData)
