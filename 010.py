"""输入描述:
输入包括两行
第一行为两个正整数n和w(1 <= n <= 30, 1 <= w <= 2 * 10^9),表示零食的数量和背包的容量。
第二行n个正整数v[i](0 <= v[i] <= 10^9),表示每袋零食的体积。

输出描述:
输出一个正整数, 表示牛牛一共有多少种零食放法。

输入例子1:
3 10
1 2 4

输出例子1:
8

例子说明1:
三种零食总体积小于10,于是每种零食有放入和不放入两种情况，一共有2*2*2 = 8种情况。
"""
t = input().split()
N = int(t[0])
W = int(t[1])
each = [int(x) for x in input().split()[:N]]
each.sort()

def count(maxi,each,temp,W):
    copy = each.copy()
    if temp>=W:
        return maxi+1
    if len(copy)==0:
        maxi+=1
    elif len(copy)>0:
        if temp+copy[0]>W:
            return maxi+1
        else:
            t = copy[0]
            copy.pop(0)
            maxi = count(maxi,copy,temp+t,W)
            maxi = count(maxi,copy,temp,W)
    return maxi

print(count(0,each,0,W))