
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.preprocessing import LabelEncoder 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
data = pd.read_csv("./input/spam_ham_dataset.csv")
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

names = [
    "MultibinomialNB",
    "Nearest Neighbors",
    "Linear SVM",
    "RBF SVM",
    "Decision Tree",
    "Random Forest",
    "LogisticRegression"
]

classifiers = [
    MultinomialNB(),
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(n_estimators=100, criterion="gini"),
    LogisticRegression(solver = 'liblinear', C=10, penalty = 'l2')
]

x, y = data.text, data.label

x_train , x_test, y_train , y_test = train_test_split(x, y, test_size=0.3)

Vectorizer = CountVectorizer()

count= Vectorizer.fit_transform(x_train.values)

clf = MultinomialNB()

targets = y_train.values

clf.fit(count, targets)

y_predict = clf.predict(Vectorizer.transform(x_test))

#Resultados de la prediccion sobre el dataset
print(y_predict)

#Valores originales de spam o ham de cada mail
print(y.values)

#Matriz de confusion del clasificador entrenado
print(confusion_matrix (y_test , y_predict))

#Precision del clasificador entrenado
print(accuracy_score(y_test, y_predict))

#Reporte de clasificacion del clasificador entrenado
print(classification_report(y_test, y_predict))
report = classification_report(y_test, y_predict, output_dict=True)
#Ejemplo prediccion de un email en particular

text = '''McAfee(TM)
Recommended by:   Lenovo
BUY NOW
Your trial expired
13 Mar 2022
Your McAfee protection expired 3 days ago

Save an extra 10% with
this email exclusive!
That's a total savings of 70%
on protection!
Get protection and save
Your all-in-one protection
includes these great features


Online privacy with Secure VPN

Award-winning antivirus

Mobile protection app

Safer web browsing

Multi-device compatibility
Award-winning internet security
Protecting more than 600 million consumer‑connected devices.
PC EDITORS CHOICE
AV TEST | TOP PRODUCT'''

test = Vectorizer.transform([text])

y_predict = clf.predict(test.astype('float32'))

print(y_predict)