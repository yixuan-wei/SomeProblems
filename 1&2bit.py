class TreeNode:
     def __init__(self, x) -> object:
         self.val = x
         self.left = None
         self.right = None


import math
import collections


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        flag = []
        nums.reverse()
        for i in range(1,length):
            for k in range(len(flag)):
                flag[k] += 1
            if nums[i] == 0:
                flag.append(0)
            j = 0
            while True:
                if j >= len(flag):
                    break
                if nums[i] > flag[j]:
                    flag.pop(j)
                else:
                    j += 1
        if len(flag) > 0:
            return False
        else:
            return True

t1 = TreeNode(3)
t2 = TreeNode(9)
t3=TreeNode(20)
t4=TreeNode(15)
t5=TreeNode(7)
t1.left=t2
t1.right=t3
t3.left=t4
t3.right=t5
words=["i", "love", "leetcode", "i", "love", "coding","i","coding"]
k=3
s = Solution()
print(s.canJump([3,0,0,0]))

