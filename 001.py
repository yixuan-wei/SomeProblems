"""
输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个正整数，表示闹钟的数量N(N<=100)。
接下来的N行每行包含两个整数，表示这个闹钟响起的时间为Hi(0<=A<24)时Mi(0<=B<60)分。
接下来的一行包含一个整数，表示从起床算起他需要X(0<=X<=100)分钟到达教室。
接下来的一行包含两个整数，表示上课时间为A(0<=A<24)时B(0<=B<60)分。
数据保证至少有一个闹钟可以让牛牛及时到达教室。


输出描述:
输出两个整数表示牛牛最晚起床时间。

输入例子1:
3
5 0
6 0
7 0
59
6 59

输出例子1:
6 0
"""
N = int(input().split()[0])
clock = []
for i in range(N):
    temp = input().split()
    clock.append([int(temp[0]),int(temp[1])])
clock.sort(key=lambda x:(x[0],x[1]))
T = int(input().split()[0])
time = input().split()
H = int(time[0])
M = int(time[1])
M = M-T
while M<0:
    M = M+60
    H = H-1
    if H<0:
        H = H+24
tH = 0
tM = 0
for each in clock:
    if each[0]<H or (each[0]==H and each[1]<=M):
        tH = each[0]
        tM=each[1]
    else:
        break
print(tH,tM)