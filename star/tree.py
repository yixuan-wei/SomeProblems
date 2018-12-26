"""
Pulsar Star Classification
Author: Yixuan Wei
2017-10-10
"""
import numpy as np
import matplotlib.pyplot as plt
import pydotplus
import graphviz

from sklearn import tree
from sklearn import model_selection
from sklearn import metrics
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

data = open('data.txt')


def create_data_set():
    dataSet = []
    labels = []
    for line in data:
        out = line.replace("\n","")
        (x1, x2, x3, x4, x5, x6, x7, x8, res) = out.split(",", 8)
        dataSet.append([float(x1), float(x2), float(x3), float(x4), float(x5), float(x6), float(x7), float(x8)])
        labels.append(res)
    return dataSet, labels


dataSet, labels = create_data_set()
X_train, X_test, y_train, y_test = model_selection.train_test_split(dataSet, labels, test_size=0.2)

# SVM
clfSVM = svm.SVC()
clfSVM.fit(X_train, y_train)
print "SVM: "
print metrics.accuracy_score(y_test, model_selection.cross_val_predict(clfSVM, X_test, y_test, cv=5))

# Naive Bayes
gnb = GaussianNB()
gnb = gnb.fit(X_train, y_train)
print "Naive Bayes: "
print metrics.accuracy_score(y_test, model_selection.cross_val_predict(gnb, X_test, y_test, cv=5))

# decision tree
clfDT = tree.DecisionTreeClassifier(splitter="random", max_depth=8, min_samples_split=100)
clfDT.fit(X_train, y_train)
print "decision tree: "
print metrics.accuracy_score(y_test, model_selection.cross_val_predict(clfDT, X_test, y_test, cv=5))

# random forest
clfRF = RandomForestClassifier(n_estimators=10)
clfRF.fit(X_train, y_train)
print "random forest: "
print metrics.accuracy_score(y_test, model_selection.cross_val_predict(clfRF, X_test, y_test, cv=5))

"""
# output tree as result.pdf
dot_data = tree.export_graphviz(clf, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("result.pdf")

# test
testSet, testLabels = create_data_set(dataTest)
predicted = model_selection.cross_val_predict(clf, testSet, testLabels)
print metrics.accuracy_score(testLabels, predicted)
"""
data.close()