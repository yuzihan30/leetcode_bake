'''
Author: your name
Date: 2022-03-27 19:10:53
LastEditTime: 2022-03-27 19:11:02
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/35_searchInsert.py
'''
class Solution:
    """
    35. 搜索插入位置
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。请必须使用时间复杂度为 O(log n) 的算法。
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 思路：二分查找的基础上，如果没找到会出现left > right的情况，跳出循环
        # left > right时，分三种情况，一种在左边，right跳到left左边界之外，
        # 另一种在右边，left跳到right右边界之外，最后一种二者都在中间，left > right
        # 1. 初始化及特殊处理
        count = len(nums)
        if count == 0:
            return 0
        l, r = 0, count-1

        # 2. 二分查找
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            
        # 3. 没有找到就返回l, 按思路分析，很容易看出返回r是错的
        return l
        # return r