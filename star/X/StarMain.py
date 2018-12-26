"""
Pulsar Star Classification
Author: Yixuan Wei
2017-10-09
"""
from X import trees

myDat, labels = trees.create_data_set()
myTree = trees.createTree(myDat, labels)
trees.storeTree(myTree, 'tree')
# print trees.classify(myTree,labels,['96.9375','37.01198075','0.563277119','1.586785985','1.606187291',
#                                    '11.91018206','12.73793927','213.6194168'])