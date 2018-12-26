"""
Pulsar Star Classification - preprocessing
Author: Yixuan Wei
2017-10-09
"""
import linecache
data = open('HTRU_2.arff', 'rU')
count = 0
for line in enumerate(data):
    count += 1
num = int(count*0.9)
"""
# output test set
target = open('data.txt', 'w')
for i in range(num, count):
    target.write(linecache.getline('HTRU_2.arff', i))
target.close()

# output training set
train = open('training.txt', 'w')
for i in range(1, num-1):
    train.write(linecache.getline('HTRU_2.arff',i))
train.close()
# output seperately negative and positive samples
posi = open('Positive.txt','w')
nega = open('Negative.txt','w')
for i in range(1, count):
    out = linecache.getline('HTRU_2.arff', i)
    j = 0
    while out[j+1] != '\n':
        j += 1
    if out[j] == '1':
        posi.write(out)
    else:
        nega.write(out)
posi.close()
nega.close()"""
data.close()
