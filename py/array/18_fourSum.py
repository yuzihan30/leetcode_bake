# -*- coding: utf-8 -*-
"""
作者：yuzihan
日期：2022年02月22日
"""
from typing import List


class Solution:
    """
    18. 四数之和
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 思路：和三数之和解决方法类似，排序加双指针，只不过多加了一层循环
        # 1. 初始化及特殊处理
        n = len(nums)
        # if not nums or n < 4 or not target: # 易错点target 可能为0
        if not nums or n < 4:
            return []
        res = []  # 存放返回结果

        nums.sort()  # 排序， 排序是双指针的前提

        # 2. 遍历
        # 第一层循环
        for i in range(n - 3):
            # 当前循环最小的四个数都大于目标值，这种情况直接退出所有循环
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # 当前循环中最大的四个数都小于目标值，就退出当前这层循环
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            # 如果当前数和后一个数相同直接跳过当前这层循环 这个不行，易错点，比如出现[0,0,0,0],目标值为0就出问题
            # if nums[i+1] == nums[i]:
            #     continue
            # 一定要注意次序，第二次遇到重复才会跳过第二个，而不是直接跳过第一个
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 第二层循环
            for j in range(i + 1, n - 2):  # 注意是从i+1开始遍历
                # 当前循环最小的四个数都大于目标值，这种情况直接退出所有循环
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # 当前循环中最大的四个数都小于目标值，就退出当前这层循环
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                # 如果当前数和后一个数相同直接跳过当前这层循环 易错点，比如出现[0,0,0,0],目标值为0就出问题
                # if nums[j+1] == nums[j]:
                #     continue
                # 一定要注意次序，第二次遇到重复才会跳过第二个，而不是直接跳过第一个
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 第三层循环：双指针
                l, r = j + 1, n - 1
                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum > target:
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif sum < target:
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum([1,0,-1,0,-2,2], 0))





