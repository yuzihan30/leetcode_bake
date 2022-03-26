'''
Author: your name
Date: 2022-03-26 22:03:34
LastEditTime: 2022-03-26 22:03:39
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/31_nextPermutation.py
'''
class Solution:
    """
    31. 下一个排列
    整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。
必须 原地 修改，只允许使用额外常数空间。
    """
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思路： 三步曲，1从右到左找到第一个比右边小的数nums[i]，
        # 2从右往左找第一个比nums[i]大的数，并交换位置， 3将nums[i]右边的序列逆序
        # 1. 初始化及特殊处理
        count = len(nums)
        if count == 0:
            return []
        # 降序排序等于本身，说明nums满足边界条件是降序排列
        if sorted(nums, reverse=True) == nums:
            # return nums[::-1] #易错点
            nums[:] = nums[::-1]
            return

        # 2. 从右到左找到第一个比右边小的数nums[i]
        # 为防止nums[i+1]越界，遍历的起始点是count-2
        for i in range(count-1)[::-1]:
            # if nums[i] > nums[i+1]:
            if nums[i] < nums[i+1]:
                break
        for j in range(i+1, count)[::-1]:
            if nums[j] > nums[i]:
                break
        nums[i], nums[j] = nums[j], nums[i]

        # 3. 将nums[i]右边的序列逆序
        # nums[i+1:] = nums[i+1::-1] #易错点
        nums[i+1:] = nums[i+1:][::-1]
