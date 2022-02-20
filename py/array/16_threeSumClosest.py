# -*- coding: utf-8 -*-
"""
作者：yuzihan
日期：2022年02月20日
"""


class Solution:
    """
    16. 最接近的三数之和
    给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
    返回这三个数的和。
    假定每组输入只存在恰好一个解。
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 思路：和求三数之和思路基本一样，稍简单，不用考虑重复问题。依然是排序后使用双指针法，排序是使用双指针法的前提
        # 1. 特殊处理+初始化
        count = len(nums)
        if count < 3:
            return NULL
        nums.sort()
        res = nums[0] + nums[1] + nums[2]

        # 2. 双指针
        for i in range(count - 2):
            left = i + 1
            right = count - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                # 更新和移动指针分开做
                if abs(target - sum) < abs(target - res):
                    res = sum
                # 注意移动指针的规则
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    return res  # 注意外层还要return一次res

        return res