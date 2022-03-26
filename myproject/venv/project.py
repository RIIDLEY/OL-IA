#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Étape 1. Importez les bibliothèques nécessaires, nous allons utiliser plus loin
import urllib.request
import os
import pandas as pd
import numpy as np
import pickle
from nltk.tokenize import RegexpTokenizer 
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import pathlib
filenameModel = '\model\\model.sav'
filenameVectorizer = '\model\\vectorizer.sav'
modelPath = str(pathlib.Path(__file__).parent)


# In[2]:


#Étape 2. Lecture du fichier .txt de Pandas et afficher les 3 premières lignes
df = pd.read_table('dataset.txt', sep=';')
df.head(3)


# In[3]:


#Étape 3. Nettoyer les données textuelles
df.isnull().sum()


# In[4]:


#supprimer les valeurs null
df = df.dropna()
df.isnull().sum()


# In[5]:


#installer nltk 
#import nltk
#nltk.download()


# In[6]:


#tester nltk 
#from nltk.corpus import brown
#brown.words()


# In[7]:


# init Objects
tokenizer = RegexpTokenizer(r'\w+')
en_stopwords=set(stopwords.words('english'))
ps=PorterStemmer()
def getStemmedReview(review):
    review=review.lower()
    review=review.replace("<br /><br />"," ")
    #Tokenize
    tokens=tokenizer.tokenize(review)
    new_tokens=[token for token in tokens if token not in  en_stopwords]
    stemmed_tokens=[ps.stem(token) for token in new_tokens]
    clean_review=' '.join(stemmed_tokens)
    return clean_review


# In[8]:


#Étape 4. Nettoyer toutes les revues et diviser nos données pour la formation et les tests.
df['review'].apply(getStemmedReview)
X_train = df.loc[:8000, 'review'].values
y_train = df.loc[:8000, 'sentiment'].values
X_test = df.loc[2000:, 'review'].values
y_test = df.loc[2000:, 'sentiment'].values


# In[9]:


#installer : pip3 install -U scikit-learn scipy matplotlib ou pip install -U scikit-learn scipy matplotlib


# In[10]:


#Étape 5. Transformer des mots en vecteurs de caractéristiques
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, encoding='utf-8',
 decode_error='ignore')
vectorizer.fit(X_train)
X_train=vectorizer.transform(X_train)
X_test=vectorizer.transform(X_test)


# In[11]:


#Étape 6. Création du modèle et vérification du score sur les données d'entraînement et de test
from sklearn.linear_model import LogisticRegression

model=LogisticRegression(solver='liblinear')
model.fit(X_train,y_train)

#print("Score on training data is: "+str(model.score(X_train,y_train)))
#print("Score on testing data is: "+str(model.score(X_test,y_test)))


#DUMP du model
# save the model to disk
pickle.dump(model, open(modelPath + filenameModel, 'wb'))
print("Sauvegarde du modele apres apprentissage réussie!")

pickle.dump(vectorizer, open(modelPath + filenameVectorizer, 'wb'))
print("Sauvegarde du vectorizer apres initialisation réussie!")


# tester sur une nouvelle valeur 
#newval = ["While the diaper pins are attractive, the metal in the pins I received are flimsy and did not hold up to the thick fabric I used them on. Fortunately there was no baby involved"]

#commentaire à analyser
#newval = ["I loved that movie. IN-CRE-DI-BLE!"]

#newval=vectorizer.transform(newval)

#retourne le résultat positif ou négatif
#model.predict(newval)

#pourcentage de positif/négatif
#model.predict_proba(newval)