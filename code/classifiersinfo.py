# ********************************************************
# *************   CREACION DE IMAGENES   *****************
# ********************************************************
from spamdetection import (plt, names, classifiers, x_test, y, y_test, y_train, count,
                        Vectorizer, classification_report, accuracy_score,
                        confusion_matrix, ConfusionMatrixDisplay)
y_axis = []
counter = 0

for claf in classifiers:
  clf = claf
  targets = y_train.values
  clf.fit(count, targets)
  
  #Resultados de la prediccion sobre el dataset
  y_predict = clf.predict(Vectorizer.transform(x_test))
  
  #Matriz de confusion del clasificador entrenado
  cm = confusion_matrix(y_test, y_predict, normalize='all') 
  cmd = ConfusionMatrixDisplay(cm, display_labels=['ham','spam'])
  cmd.plot()

  # Creacion de imagen    
  plt.savefig('./images/' + names[counter] + '.jpg')

  #Precision del clasificador entrenado
  acc = accuracy_score(y_test, y_predict)
  acc = acc * 100
  y_axis.append(acc)

  #Reporte de clasificacion del clasificador entrenado
  report = classification_report(y_test, y_predict, output_dict=True)
  
  counter = counter + 1
  plt.clf()

colors = ['blue', 'maroon', 'yellow', 'red', 'green', 'pink', 'purple']
plt.bar(names, y_axis, color = colors, width = 0.4)
plt.title('Accuracy scores of each classifier')
plt.xlabel('Classifiers')
plt.xticks(fontsize = 5, rotation = 30)
plt.ylabel('Accuracy score')
plt.savefig('./images/Accuracy.jpg')