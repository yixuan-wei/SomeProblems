"""
Pulsar Star Classification - decision tree from 0
---unable to process successfully
Author: Yixuan Wei
2017-10-09
"""

import operator
from math import log

data = open('training.txt')


def create_data_set():
    dataSet = []
    for each_line in data:
        out = each_line.replace("\n", "")
        (x1, x2, x3, x4, x5, x6, x7, x8, res) = out.split(",", 8)
        dataSet.append([float(x1), float(x2), float(x3), float(x4), float(x5), float(x6), float(x7), float(x8), res])
    labels = ['Mean of the integrated profile', 'Standard deviation of the integrated profile',
              'Excess kurtosis of the integrated profile',
              'Skewness of the integrated profile', 'Mean of the DM-SNR curve',
              'Standard deviation of the DM-SNR curve', 'Excess kurtosis of the DM-SNR curve',
              'Skewness of the DM-SNR curve']
    return dataSet, labels


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    # set up dic for all labels
    labelCounts = {}
    for featVec in dataSet:
        # to get the last row of data
        currentLable = featVec[-1]
        if currentLable not in labelCounts.keys():
            labelCounts[currentLable] = 0
        labelCounts[currentLable] += 1
    # calculate Shannon Ent
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


# split data set by 3 input parameters: raw data set, feature, classifying value
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if float(featVec[axis]) == float(value):
            reduceFeatVec = featVec[:axis]
            reduceFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet


# to choose the best feature to split
def chooseBestFeatureToSplit(dataSet):
    numFeature = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInforGain = 0
    bestFeature = -1
    for i in range(numFeature):
        featList = [number[i] for number in dataSet]  # all values of a certain feature
        uniqualVals = set(featList)
        newEntropy = 0
        for value in uniqualVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)  # sum up
        infoGain = baseEntropy - newEntropy
        # best info gain
        if (infoGain > bestInforGain):
            bestInforGain = infoGain
            bestFeature = i
    return bestFeature


# vote for best code
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    # stop if feature remains
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    # choose the best feature to split
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLable = labels[bestFeat]
    myTree = {bestFeatLable: {}}  # set up dic for tree
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLables = labels[:]
        myTree[bestFeatLable][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLables)
    return myTree


def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'wb')  # binary storing
    pickle.dump(inputTree, fw)
    fw.close()


# to classify test sample by tree
def classify(inputTree, featLables, testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLables.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLables, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel
