'''
Author: your name
Date: 2022-04-10 12:38:19
LastEditTime: 2022-04-10 14:48:32
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/41_firstMissingPositive.py
'''
class Solution:
    """
    41. 缺失的第一个正数
    给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
    请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 思路：采用两数互换的方式让数组中位于闭区间[1,n]的正整数，回到自己的位置上，
        # 即将nums[i]回到nums[nums[i] - 1]的位置， 即满足nums[i] = i + 1
        # 1. 初始化及特殊处理
        if not nums:
            return 1
        count = len(nums)

        # 2. 遍历交换位置
        for i in range(count):
            # 易错点：注意是while循环，因为交换一次之后，nums[i]和nums[nums[i] - 1]还是满足条件
            # 另外判断条件是nums[nums[i] - 1] 而不是nums[i], 根据nums[i] != i + 1是不准确的
            # if nums[i] >= 1 and nums[i] <= count and nums[i] != i + 1:
            # while nums[i] >= 1 and nums[i] <= count and nums[i] != i + 1:
            # while nums[i] >= 1 and nums[i] <= count and nums[nums[i]-1] != nums[i]:
            # 疑点1：为何这个while循环是常数级别复杂度， 因为while循环过的，交互过的位置必然满足条件，
            # for循环就不用处理，for 和while循环加在一起是O(n)复杂度
            while 1<= nums[i] <= count and nums[nums[i]-1] != nums[i]:
                # 疑点2：为何上面这种交换方式会超时，而下面不会， 因为上面这种计算方式，
                # 可能会将nums[i]先替换掉，导致再计算左边的nums[nums[i] - 1]时，nums[i]已经改变
                # nums[nums[i] - 1]和nums[i]有依赖关系，所以要注意先后次序
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # 3. 遍历找第一个不匹配自己位置的元素（元素的索引）
        for i in range(count):
            if nums[i] != i + 1:
                return i + 1

        # 4. 遍历完都满足条件则返回末尾元素的值加1, 或者返回数组长度加1
        return count + 1