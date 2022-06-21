class Solution:
    """
    34. 在排序数组中查找元素的第一个和最后一个位置
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
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