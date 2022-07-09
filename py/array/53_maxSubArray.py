class Solution:
    """
    53. 最大子数组和
    给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分
    """
    def maxSubArray(self, nums: List[int]) -> int:
        # 思路：动态规划（dynamic programming），核心是，遍历nums时，dp列表内依次存入nums[i]
        # 结尾的连续数组的最大值；如果dp[i-1]小于0，则dp[i]为nums[i], 否则dp[i]=dp[i-1]+nums[i]
        # 1. 初始化及特殊处理
        num = len(nums)
        dp = [None] * num
        dp[0] = nums[0]
        max_value = nums[0]

        # 2. 遍历
        for i in range(1, num):
            dp[i] = nums[i] + dp[i-1] if dp[i-1] > 0 else nums[i]
            max_value = max(max_value, dp[i])
        
        # 3. 返回结果值
        return max_value