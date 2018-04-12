"""
峰值元素是指其值大于左右相邻值的元素。
给定一个输入数组，其中 num[i] ≠ num[i+1]，找到峰值元素并返回其索引。
数组可能包含多个峰值，在这种情况下，返回到任何一个峰值所在位置都可以。
你可以想象得到  num[-1] = num[n] = -∞。
例如，在数组 [1, 2, 3, 1]中 3 是峰值元素您的函数应该返回索引号2
复杂度对数
"""
class Solution:
    def findPeakElement(self,nums):
        if len(nums) == 0 or len(nums) == 1:
            return 0

        def findp(nums, l, r):
            if l == r:
                return 0
            half = int((l + r) / 2)
            if half - l > 0:
                if nums[half] > nums[half - 1]:
                    if nums[half] > nums[half + 1]:
                        return half
                    else:
                        left = findp(nums, l, half - 1)
                        right = findp(nums, half, r)
                        if right > 0:
                            return right
                        else:
                            return left
                elif nums[half] < nums[half - 1]:
                    if half == 1:
                        return 0
                    left = findp(nums, l, half)
                    right = findp(nums, half + 1, r)
                    if nums[left] > nums[right]:
                        return left
                    else:
                        return right
                else:
                    left = findp(nums, l, half - 1)
                    right = findp(nums, half + 1, r)
                    if left > 0:
                        return left
                    else:
                        return right
            else:
                if nums[half]>nums[r]:
                    return half
                else:
                    return r
        return findp(nums, 0, len(nums) - 1)

s = Solution()
print(s.findPeakElement([4,3,2,1]))