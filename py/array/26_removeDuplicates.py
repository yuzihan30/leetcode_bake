'''
Author: your name
Date: 2022-03-08 22:27:52
LastEditTime: 2022-03-08 22:28:07
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/26_removeDuplicates.py
'''
class Solution:
    """
    26. 删除有序数组中的重复项
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        # 思路：双指针法（快慢指针），快指针遇到和前面值不同的就填充到慢指针的位置
        # 1. 初始化及特殊处理
        if not nums:
            return 0
        n = len(nums)
        # 第一个数处理完后在原数组中不动，所以索引从1开始处理
        fast = slow = 1 
        # 2. 遍历
        while fast < n:
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1  # 只有慢指针处被填充值时才会移动
            fast += 1  # 快指针每次都要移动

        # 3. 返回结果，当fast遍历完时，当前slow索引位置还未填充值，
        # 极端情况下原数组元素都不同，slow总是先于fast指针移动一步，最终slow移出循环时，
        # slow索引处并未填充值；其他情况类似，slow指向的最后一个空缺总是未来得及填充，
        # 所以返回slow即为slow索引前面元素的长度
        return slow