from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn import preprocessing
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np

glass_data = pd.read_csv('../glass.csv')

label_encoder = preprocessing.LabelEncoder()
data = glass_data
iris_data = label_encoder.fit_transform(glass_data.values[:, 9])

X = data.values[:, :4]
Y = iris_data

model = GaussianNB()
kf = KFold(n_splits=15, shuffle=True,random_state=50)
accuracy = []

for train_index, test_index in kf.split(X):
   X_train, X_test = X[train_index], X[test_index]
   Y_train, Y_test = Y[train_index], Y[test_index]

   #Training the model
   model.fit(X_train, Y_train)

   #Predictions
   y_pred = model.predict(X_test)

   #Accuracy score
   print("Accuracy score: ", metrics.accuracy_score(Y_test, y_pred))
   accuracy.append(metrics.accuracy_score(Y_test, y_pred))

   #Confusion Matrix
   confusionmatrix = confusion_matrix(Y[test_index], y_pred)
   print(confusionmatrix)

#Mean Accuracy
print("Mean Accuracy Score: ", np.mean(accuracy))