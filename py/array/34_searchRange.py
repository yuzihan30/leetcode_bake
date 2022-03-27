'''
Author: your name
Date: 2022-03-27 12:34:29
LastEditTime: 2022-03-27 12:34:33
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/34_searchRange.py
'''
class Solution:
    """
    34. 在排序数组中查找元素的第一个和最后一个位置
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 思路： 二分查找，关键是怎么在无重复元素二分查找基础上修改
        # 参考视频：https://www.bilibili.com/video/BV1aF411H7fn?spm_id_from=333.337.search-card.all.click
        # 1. 初始化及特殊处理
        count = len(nums)
        if count == 0:
            return [-1, -1]
        
        # 2. 查找首个和最后一个位置
        first = self.binarySearchFirst(nums, target)
        last = self.binarySearchLast(nums, target)

        # 3. 返回结果值
        return [first, last]

    def binarySearchFirst(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                # return mid
                # 这里是关键点，与无重复有序数组二分查找的差别
                # 想确定mid是第一个，则需确认mid前无重复值，或者mid就是第一个数组元素
                if mid == 0 or nums[mid - 1] != nums[mid]:
                    return mid
                # mid不是第一个目标值，则需要继续向前找
                else:
                    r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else: 
                r = mid - 1

        return -1

    def binarySearchLast(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                # return mid
                # 这里是关键点，与无重复有序数组二分查找的差别
                # 想确定mid是最后一个，则需确认mid后无重复值，或者mid就是最后一个数组元素
                if mid == len(nums)-1 or nums[mid+1] != nums[mid]:
                    return mid
                # mid不是第一个目标值，则需要继续向前找
                else:
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else: 
                r = mid - 1

        return -1   