'''
Author: your name
Date: 2022-05-03 21:23:25
LastEditTime: 2022-05-03 21:34:10
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/45_jump.py
'''
class Solution:
    """
    45. 跳跃游戏 II
    给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。
    """
    def jump(self, nums: List[int]) -> int:
        # 思路：这里采用贪心思想，也可以用递归等方法，贪心最优， 每次都跳到当前位置能跳到最大位置
        # 1. 初始化及特殊处理
        if not nums:
            return 0
        count = len(nums)
        curMaxIndex = 0  # 记录当前能跳的最远位置
        nextMaxIndex = 0  # 记录下一步能跳最远的位置
        stepNum = 0  # 记录步数

        # 2. 遍历，注意只需要遍历到倒数第二个位置
        # 题目说你总是可以到达数组的最后一个位置，说明达到最后一个位置前的最坏情况是在倒数第二个位置
        for i in range(count - 1):
            # 易错点
            # nextMaxIndex = max(i + nums[i], curMaxIndex)
            nextMaxIndex = max(i + nums[i], nextMaxIndex)
            # 当前正好在最大位置上，不得不跳，这时需要更新步数
            if i == curMaxIndex:
                curMaxIndex = nextMaxIndex
                stepNum += 1
        
        # 3. 返回结果值
        return stepNum