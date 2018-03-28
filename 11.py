"""
输入前四个分别表示后面四个值个数的八个数字，寻找最好的一种排列所有这四种值的方式，
使得过程中当前数字和的个位数与新加入的数的乘积的总和最大，输出最大乘积和
"""
import sys
for line in sys.stdin:
    a = input().split()
    nums = [int(a[i]) for i in range(4)]
    mass = [int(a[i]) for i in range(4,8)]
    used = [0]*4
    maxi=0

    def findmax(nums,mass,maxi):
        if sum(nums)==0:
            maxi = 0
        else:
            used = nums.copy()
            for i in range(4):
                if used[i]>0:
                    used[i]-=1
                    new = mass[i]*(sum(mass[j]*used[j] for j in range(4))%10)
                    return max(maxi,findmax(used,mass,maxi)+new)
        return maxi

    print(findmax(nums,mass,maxi))