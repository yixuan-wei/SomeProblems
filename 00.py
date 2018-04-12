"""
输入描述:
输入包括两个整数l和r(1 <= l <= r <= 1e9), 表示要求解的区间两端。

输出描述:
输出一个整数, 表示区间内能被3整除的数字个数。

输入例子1:
2 5

输出例子1:
3

例子说明1:
12, 123, 1234, 12345...
其中12, 123, 12345能被3整除。
"""
def incre(l,m):
    l[m]+=1
    if l[m]==0:
        incre(l,m+1)

def sumn(n):
    if n<10:
        return n
    return n%10+sumn(int(n/10))


t = input().split()
l = int(t[0])
r = int(t[1])
first=0
for i in range(l):
    first+=sumn(i+1)
res=0
re = [0]*10
if first%3==0:
    res+=1
    first = first%3
le = l
k=0
while le>0:
    re[k] = le%10
    le = int(le/10)
    k+=1
for j in range(l+1,r+1):
    incre(re,0)
    first+=sum(re)
    if first%3==0:
        res+=1
        first = 0
print(res)