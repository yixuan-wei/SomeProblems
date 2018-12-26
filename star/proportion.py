"""
Pulsar Star Classification
Author: Yixuan Wei
2017-10-10
"""
from sklearn import tree
from sklearn import model_selection
from sklearn import metrics

posi = open('Positive.txt')
nega = open('Negative.txt')
out11 = open('11', 'r')
out12 = open('12', 'r')
out14 = open('14', 'r')
out18 = open('18', 'r')


def create_out():
    line = nega.readline()
    for each_line in posi:
        out18.write(each_line)
        for i in range(1,9):
            out18.write(line)
            line = nega.readline(153071)
    return


def create_data_set():
    dataSet = []
    labels = []
    for each_line in out18:
        out = each_line.replace("\n","")
        (x1, x2, x3, x4, x5, x6, x7, x8, res) = out.split(",", 8)
        dataSet.append([float(x1), float(x2), float(x3), float(x4), float(x5), float(x6), float(x7), float(x8)])
        labels.append(res)
    return dataSet, labels


#create_out()
dataSet, labels = create_data_set()
X_train, X_test, y_train, y_test = model_selection.train_test_split(dataSet, labels, test_size=0.2)

# decision tree
clfDT = tree.DecisionTreeClassifier(splitter="random", max_depth=8, min_samples_split=100)
clfDT.fit(X_train, y_train)
predicted = model_selection.cross_val_predict(clfDT, X_test, y_test, cv=5)
print "decision tree accuracy score: "
print metrics.accuracy_score(y_test, predicted)

posi.close()
nega.close()
out11.close()
out12.close()
out14.close()
out18.close()