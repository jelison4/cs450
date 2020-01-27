from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import datasets
iris = datasets.load_iris()

# Show the data (the attributes of each instance)
# print(iris.data)
#
# Show the target values (in numeric format) of each instance
# print(iris.target)
#
# Show the actual target names that correspond to each number
# print(iris.target_names)

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.30, random_state=44)

# print(X_train)
#print(y_train)

classifier = GaussianNB()
classifier.fit(X_train, y_train)
targets_predicted = classifier.predict(X_test)


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


accuracy = clacAccuracy(targets_predicted, y_test)

print(f"The model is {accuracy}% accurate")

class HardCodedClassifier:
    def fit(self, data_train, targets_train):
        print("Fitting...")
        return 0

    def predict(self, data):
        prediction = []
        
        dataLength=len(data)
        i=0

        while i < dataLength:
            prediction.append(1)
            i+=1
        return prediction
    
classifier = HardCodedClassifier()
classifier.fit(X_test, y_test)

targets_predicted1 = classifier.predict(y_test)

hardCodedAccuracy=clacAccuracy(targets_predicted1, y_train)
print(f"The hardcoded model is {hardCodedAccuracy}% accurate")