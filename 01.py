"""
输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个正整数，表示转方向的次数N(N<=1000)。
接下来的一行包含一个长度为N的字符串，由L和R组成，L表示向左转，R表示向右转。

输出描述:
输出牛牛最后面向的方向，N表示北，S表示南，E表示东，W表示西。

输入例子1:
3
LRR

输出例子1:
E
"""
def direction(m,n):
    if (m=='N' and n=='L') or (m=='S' and n=='R'):
        return 'W'
    elif (m=='N' and n=='R') or (m=='S' and n=='L'):
        return 'E'
    elif (m,n)==('W','L') or (m,n=='E','R'):
        return 'S'
    elif (m,n=='W','R') or (m,n)==('E','L'):
        return 'N'

N = int(input().split()[0])
D = list(input().split()[0])
new='N'
for i in range(N):
    new = direction(new,D[i])
print(new)