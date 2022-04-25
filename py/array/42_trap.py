'''
Author: your name
Date: 2022-04-25 09:07:14
LastEditTime: 2022-04-25 09:07:27
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/42_trap.py
'''
class Solution:
    """
    42. 接雨水
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    """
    def trap(self, height: List[int]) -> int:
        # 思路：动态规划，将左右最小高度分别存储到两个数组里，当前柱子i对应的接水量
        # 等于左右两侧柱子高度的最小值减去当前柱子的高度，如果两边都比当前柱子低就取0
        # 1. 初始化及特殊处理
        n = len(height)
        if n < 3:
            return 0
        ans = 0
        left_h = [0] * n
        max_left = height[0]
        left_h[0] = height[0]
        right_h = [0] * n
        max_right = height[n-1]
        right_h[n-1] = height[n-1]

        # 2. 递推求左右最高值数组
        for i in range(1, n):
            left_h[i] = max(left_h[i-1], height[i])
        
        for j in range(n-2, -1, -1):
            right_h[j] = max(right_h[j+1], height[j])

        # 3. 遍历求总和
        for k in range(n):
            ans += max(0, min(left_h[k], right_h[k]) - height[k])

        # 4. 返回结果值
        return ans