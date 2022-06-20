from typing import List
class Solution:
    """
    15. 三数之和
    给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？
    请你找出所有和为0且不重复的三元组。注意：答案中不可以包含重复的三元组。
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 思路：直接上双指针法，关键是将三数之和转化成两数之和问题，并去重（排序，并且内、外层循环相同数跳过）
        # 1、特殊处理、初始化
        count = len(nums)
        res = []
        if count < 3:
            return []

        # 2、排序
        nums.sort()  # 去重三重奏，一排序
        # 3、遍历
        for i in range(count - 2):  # 注意点：是count - 2
            # 去重三重奏，二外层相同数跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 转化为求两数之和, 双指针法
            target = -nums[i]
            left = i + 1
            right = count - 1
            while left < right:
                sum = nums[left] + nums[right]
                if target == sum:
                    res.append([nums[i], nums[left], nums[right]])
                    left = left + 1
                    right = right - 1
                    # 内层循环中双指针移动时遇到相同数跳过
                    while left < right and nums[left] == nums[
                        left - 1]:  # 易错点：nums[left] == nums[left-1] 不是nums[left+1]
                        left = left + 1
                    while left < right and nums[right] == nums[
                        right + 1]:  # 易错点：nums[right] == nums[right+1] 不是nums[right - 1]
                        right = right - 1
                elif target < sum:
                    right = right - 1
                else:
                    left = left + 1

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
