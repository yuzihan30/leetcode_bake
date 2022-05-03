'''
Author: your name
Date: 2022-05-03 22:07:55
LastEditTime: 2022-05-03 22:08:02
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/55_canJump.py
'''
class Solution:
    """
    55. 跳跃游戏
    给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。
    """
    def canJump(self, nums: List[int]) -> bool:
        # 思路：贪心思想，遍历，每次更新当前能跳的最远距离，
        # 如果最远距离超过最大下标就返回True, 否则如果当前位置正好是当前能跳的最远距离返回False
        # 1. 初始化
        count = len(nums)
        maxIndex = 0  # 初始化当前能跳的最远距离

        # 2. 遍历并返回结果
        for i in range(count):
            # maxIndex = max(i + nums[i], maxIndex)
            if i + nums[i] > maxIndex:
                maxIndex = i + nums[i]
            if maxIndex >= count - 1:
                return True
            elif i == maxIndex:
                return False
        
        # 3. 返回结果 这个返回其实没有意思，假设遍历完没有返回值，这种情况是不存在的
        # return True