"""
Clustering by Knn - A simple example
author: Yixuan Wei
2017-10-09
"""
import math
data = open('./Input.txt')
# para[] for two parameters in data; label[] for corresponding labels & distance to (273, 230)
para = []
label = []
result = [['1', 0], ['2', 0], ['3', 0]]  # scores for three classes
try:
    for each_line in data:
        try:
            # clear redundant "()"
            out = each_line.replace("(", "").replace(")", "").replace("\n", "")
            (x11, x21, _label) = out.split(",", 2)
            x1 = int(x11)
            x2 = int(x21)
            # calculate every point's distance to target (273, 230)
            _dis = math.sqrt((x1-273)*(x1-273)+(x2-230)*(x2-230))
            para.append([x1, x2])
            label.append((_label, _dis))
        except ValueError:
            pass
    # sort label by distance from small to large
    label.sort(key=lambda k: k[1])
    for i in range(0, 5):   # 5-nn algorithm
        Label = label[i][0]
        if Label == '1':
            result[0][1] += 1
        elif Label == '2':
            result[1][1] += 1
        else:
            result[2][1] += 1
    result.sort(key=lambda k: k[1])
    print "target (273, 230) is expected to be classified as class " +result[2][0]
finally:
    data.close()