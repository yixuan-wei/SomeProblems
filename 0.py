"""
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
保证不存在两项工作的报酬相同。

输出描述:
对于每个小伙伴，在单独的一行输出一个正整数表示他能得到的最高报酬。一个工作可以被多个人选择。

输入例子1:
3 3
1 100
10 1000
1000000000 1001
9 10 1000000000

输出例子1:
100
1000
1001
"""
t = input().split()
N = int(t[0])
M = int(t[1])
works = []
i=0
while i<N:
    temp = input().split()
    if temp:
        works.append([int(temp[0]),int(temp[1])])
        i+=1
people = []
tt = input().split()
while tt==[]:
    tt = input().split()
people.extend(int(e) for e in tt)
works.sort(key=lambda x:(x[0],x[1]))
it = [-1,-1]
for each in works:
    if each[0]==it[0]:
        works.remove(it)
    it = each
print(works)
for each in people:
    maxi=0
    for j in range(len(works)):
        if works[j][0]<=each:
            maxi = max(maxi,works[j][1])
        else:
            break
    print(maxi)
