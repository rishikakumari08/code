#libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

iris=pd.read_csv("Iris.csv")
print(iris.head())
iris.info
print(iris.describe)

#train
train,test=train_test_split(iris,test_size=0.25)
train
# test
test
train_x=train[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
train_y=train.Species
print(train_x)
print(train_y)
test_x=test[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
test_y=test.Species

#svm
model=svm.SVC()
model.fit(train_x,train_y)
pred=model.predict(test_x)
accuracy=metrics.accuracy_score(pred,test_y)
print("accuracy is: ",accuracy)

#Desicion
model=DecisionTreeClassifier()
model.fit(train_x,train_y)
pred=model.predict(test_x)
accuracy=metrics.accuracy_score(pred,test_y)
print("now the Desicion accuracy is: ",accuracy)

#graph
plt.figure(figsize=(12,10))
plt.title("iris SepalLength")
sns.histplot(x="SepalLengthCm",hue="Species",data=iris)
plt.show()

plt.figure(figsize=(12,10))
plt.title("iris SepalWidth")
sns.histplot(x="SepalWidthCm",hue="Species",data=iris)
plt.show()

plt.figure(figsize=(12,10))
plt.title("iris PetalLength")
sns.histplot(x="PetalLengthCm",hue="Species",data=iris)
plt.show()

plt.figure(figsize=(12,10))
plt.title("iris PetalWidth")
sns.histplot(x="PetalWidthCm",hue="Species",data=iris)
plt.show()