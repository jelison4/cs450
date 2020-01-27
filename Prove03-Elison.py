import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

carHeader = ["buying", "maint",
             "doors", "persons", "lug_boot", "safety", "value"]

carData = pd.read_csv(
    "week03data/car.data",
    header=None, names=carHeader, na_values="?")

# print(carData)
carData.head

mpgHeader = ["mpg", "cylinders", "displacment", "horsepower",
             "weight", "acceleration", "model", "origin", "car_name"]
mpgData = pd.read_csv("week03data/auto-mpg.data",
                      header=None, names=mpgHeader, na_values="?")

print(mpgData)
mpgData.head

studentHeader = []
studentDAta = pd.read_csv("week03data/student-mat.csv", na_values="?")

print(studentDAta)
