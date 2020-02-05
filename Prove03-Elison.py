import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#######################################################################
# Accuracy Calculator
#######################################################################


def clacAccuracy(results, test):
    count = len(results)
    right = 0
    i = 0

    while i < count:
        iResult = results[i]
        iTest = test[i]
        if iResult == iTest:
            right += 1
        i += 1

    accuracy = round((right/count)*100, 2)

    return accuracy

#######################################################################
# KNN Stuff
#######################################################################


def KNNAccuracy(data, target, k):
    X_train, X_test, y_train, y_test = train_test_split(
        data, target, test_size=0.30, random_state=42)

    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(X_train, y_train)
    predictions = classifier.predict(X_test)
    accuracy = clacAccuracy(predictions, y_test)

    return accuracy

#######################################################################
# Regression junk
#######################################################################


def regressionAccuracy(data, target):
    X_train, X_test, y_train, y_test = train_test_split(
        data, target, test_size=0.2, random_state=24)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)

    predActualDelta = []

    count = 0
    for i in y_pred:
        predActualDelta.append(i-y_test[count])
        count += 1

    return abs(sum(predActualDelta)/len(predActualDelta))


#######################################################################
# Car Data
#######################################################################
carHeader = ["buying", "maint",
             "doors", "persons", "lug_boot", "safety", "value"]

carDp = pd.read_csv("week03data/car.data",
                    header=None, names=carHeader, na_values="?")

# print(carDp)
catList = ["buying", "maint", "lug_boot", "safety", "value"]
carDp[catList] = carDp[catList].astype('category')

carDp["buying"] = carDp["buying"].cat.codes
carDp["maint"] = carDp["maint"].cat.codes
carDp["lug_boot"] = carDp["lug_boot"].cat.codes
carDp["safety"] = carDp["safety"].cat.codes
carDp["value"] = carDp["value"].cat.codes

cleanupNums = {"doors": {"5more": 5},
               "persons": {"more": 5}}

# Making all the data types the same
carDp.replace(cleanupNums, inplace=True)
carDp[["doors", "persons"]] = carDp[["doors", "persons"]].astype('int8')

# putting data frames into numpy arrays
carData = np.array(carDp[["buying", "maint",
                          "doors", "persons", "lug_boot", "safety"]])
carTarget = np.array(carDp.value)

# Setting k for the cars
cark = 5
carAccuracy = KNNAccuracy(carData, carTarget, cark)
print(
    f"After data was cleaned KNN with k={cark} was able to predict the value of the car correctly {carAccuracy}% of the time")

#######################################################################
# MPG Data
#######################################################################
mpgHeader = ["mpg", "cylinders", "displacment", "horsepower",
             "weight", "acceleration", "model", "origin", "name"]
mpgDp = pd.read_csv("week03data/auto-mpg.data",
                    header=None, sep='\s+', names=mpgHeader, na_values="?")

# The only null values are in the horsepower column.
# To solve this I set the missing hoursepower values equal to the average horsepower
meanHp = mpgDp.loc[:, "horsepower"].mean()
mpgDp = mpgDp.fillna({"horsepower": meanHp})

# The names are super varied and could largly affect the outcome if simply encoded.
# Dropping the column seemed the best option for the data
mpgDp = mpgDp.drop(columns=["name"])

mpgData = np.array(mpgDp[["cylinders", "displacment", "horsepower",
                          "weight", "acceleration", "model", "origin"]])
mpgTarget = np.array(mpgDp.mpg)

mpgAccuracy = round(regressionAccuracy(mpgData, mpgTarget), 3)
print(
    f"After data was cleaned the regression model was able to predict mpg with a mean differance between the prediction and real value of {mpgAccuracy}")

#######################################################################
# Student Data
#######################################################################
studentDf = pd.read_csv("week03data/student-mat.csv", sep=';', na_values="?")

# Make a list of the categories that will be label encoded
catList1 = ["school", "sex", "address", "famsize", "Pstatus", "schoolsup", "romantic",
            "internet", "guardian", "Mjob", "Fjob", "famsup", "paid", "activities", "nursery", "higher"]

# Set the data type of the columns in the catList1 as category 
studentDf[catList1] = studentDf[catList1].astype('category')


for i in catList1:
    studentDf[i] = studentDf[i].cat.codes

# One hot encode the reason for choosing the school
studentDf = pd.get_dummies(studentDf, columns=["reason"]).head()

stuData = studentDf.drop(columns=["G3"])

stuTarget = np.array(studentDf.G3)

stuAccuracy = round(regressionAccuracy(stuData, stuTarget), 3)
print(
    f"After data was cleaned the regression model was able to predict Student grades with a mean differance between the prediction and real value of {stuAccuracy}")
