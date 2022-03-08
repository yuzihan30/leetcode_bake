'''
Author: your name
Date: 2022-03-08 22:48:21
LastEditTime: 2022-03-08 22:48:28
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/27_removeElement.py
'''
class Solution:
    """
    27. 移除元素
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