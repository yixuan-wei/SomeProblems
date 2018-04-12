"""
输入描述:
输入包括两个正整数n,k(1 <= n <= 10^5, 0 <= k <= n - 1)。

输出描述:
对于每个测试用例, 输出一个正整数表示可能的数对数量。

输入例子1:
5 2

输出例子1:
7

例子说明1:
满足条件的数对有(2,3),(2,4),(2,5),(3,4),(3,5),(4,5),(5,3)
"""
l = input().split()
n = int(l[0])
m = int(l[1])
if m==0:
    res=0
else:
    res = int((n-m)*(n-m+1)/2)
i = m+1
remain = m
while i <= n:
    p=1
    while p*i+m<=n:
        q = i-1
        q = min(n-p*i,q)
        if q>=m:
            res+=q-m+1
        p+=1
    i+=1
print(res)