class Solution:
    """
    33. 搜索旋转排序数组
    整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
    """
    def search(self, nums: List[int], target: int) -> int:
        # 思路：二分查找利用部分有序特征，分左半边有序无序两种情况处理，左边有序时右边无序，左边无序右边有序
        # 1. 初始化及特殊处理
        count = len(nums)
        if count == 0:
            return -1
        l, r = 0, count - 1
        # mid = (l+r) // 2

        # 2. 二分查找
        # while l < r: # 易错点：比如[7], 找7
        while l <= r:
            mid = (l+r) // 2
            # 2.1 如果nums[mid] == target, 则直接返回mid
            if nums[mid] == target:
                return mid
            # 2.2 左边有序
            # if nums[l] < nums[mid]:
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                # 右边无序，且可能在右边， 走while循环重新执行二分法
                else:
                    l = mid + 1
            # 2.3 右边有序
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                # 左边无序，且可能在左边， 走while循环重新执行二分法
                else:
                    r = mid - 1


        # 3. 循环完后未找到，则返回-1未找到
        return -1
        