class Solution:
    """
    27. 移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        # 思路：双指针法，当右指针指向的元素不等于val时填充到做指针处
        # 1. 初始化及特殊处理
        if not nums:
            return 0
        n = len(nums)
        fast = slow = 0

        # 2. 遍历
        while fast < n:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        # 3. 返回结果值
        return slow