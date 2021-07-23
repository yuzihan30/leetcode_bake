"""
1. 两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值target的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 理解题目：从题目中语句"请你在该数组中找出和为目标值target的那两个整数，数组中同一个元素在答案里不能重复出现"
        # 可以看出列表是没有重复值的
        # 1. 创建字典，a:将列表中值为key, 索引作为值保存到字典中（为何值作为key，方便根据值快速获取索引，如果索引作为key，
        # 就很难快速根据值获取索引）b. 字典类型查询快
        dict = {}
        # 2. 遍历列表, 
        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
        # 一般用在 for 循环当中
        for index, num in enumerate(nums):
            # 关键点1：拿到配对值, 可以不定义couple变量，但定义该变量程序可读性更好，并可减少target - num的重复计算
            couple = target - num
            # 判断字典中键是否存在：pyton3中支持key in dict 或者 key in dict.keys()
            # python2中dict.has_key(key)
            if couple in dict:
                # 当前遍历元素的索引是index，已遍历过的元素存储在dict中，类似于左侧查找配对元素
                return [dict[couple], index] 
            else:
                dict[num] = index 

"""
leetcode上执行结果：
执行用时：24 ms, 在所有 Python 提交中击败了67.78%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了33.94%的用户
同样的代码提交第二次：
执行用时：12 ms, 在所有 Python 提交中击败了98.45%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了64.12%的用户
"""