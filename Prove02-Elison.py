# -*- coding: utf-8 -*-
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def calcDistance(x,y):
    i=0
    distance = 0
    while i < len(x):
        distance += (x[i]-y[i])**2
        i+=1
    return distance

def getDistances(point, data):
    distances=np.empty(0, dtype=float)
    for i in data:
        dist = calcDistance(point,i)
        distances=np.append(distances, dist)
    return distances

def most_frequent(List): 
    return max(set(List), key = List.count)

def KNNClassifier(k, distances, y_data):
    lowest=distances.argsort()[:k]
    neighbors=[]
    for x in lowest:
        neighbors.append(y_data[x])
    return most_frequent(neighbors)

def test(k, X_train, X_test, y_train, y_test):
    count = 0
    correct=0
    for i in X_test:
        distances=getDistances(i, X_train)
        guess=KNNClassifier(k, distances, y_train)
        if(guess==y_test[count]):
            correct+=1
        count+=1
    return round(correct/count*100, 2)

def clacAccuracy(results, test):
    count=len(results)
    right = 0
    i=0
    
    while i < count:
        iResult=results[i]
        iTest=test[i]
        if iResult==iTest:
            right+=1
        i += 1

    accuracy = round((right/count)*100, 2)

    return accuracy

iris = datasets.load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.30, random_state=44)

k = 1
while k <= 10:
    accruacy=test(k, X_train, X_test, y_train, y_test)
    print(f"My own KNN algorithm with k={k} is {accruacy}% accurate")
    k += 1
    
j = 1
while j <= 10:
    classifier = KNeighborsClassifier(n_neighbors=j)
    classifier.fit(X_train, y_train)
    predictions = classifier.predict(X_test)
    impAccuracy=clacAccuracy(predictions, y_test)
    print(f"The exixting implementation of the KNN algorithm with k={j} is {impAccuracy}% accurate")
    j += 1